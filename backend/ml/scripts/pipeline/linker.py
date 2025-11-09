import json
import yaml
import os
from pathlib import Path
from tqdm import tqdm
import logging
import sys
sys.path.insert(0, '../')
from modules.document.models import JsonType
from utils.job_utils import get_all_jsons_for_json_type, read_json_from_db
from ml.scripts.core.config_loader import ConfigLoader

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UsdmSchemaLinker:
    def __init__(self, output_dir, document_id):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"UsdmSchemaLinker initialized. Output directory: {output_dir}")

        self.schemas_dir = os.path.join(output_dir, 'connected_schemas')
        self.config_loader = ConfigLoader()
        self.config_data = self.config_loader.get_config_data()
        self.usdm_data_dictionary = self.config_data['usdm_data_dictionary']
        self.output_dir = output_dir
        self.document_id = document_id
        self.schema_data = {}
        self.schema_files = []
        self.current_path = []  # Track current processing path to detect circular references
        self.circular_references = set()  # Track detected circular references
        self.used_schemas = set()  # Track which schemas are used in linking
        self.unused_schemas = set()  # Track which schemas are not used in linking
        
    def load_data(self):
        # Find all JSON files in the base directory
        # self.logger.info("Finding JSON schema files")
        json_files = list(Path(self.schemas_dir).glob("*.json"))
        self.schema_files = [f.name for f in json_files]
        
        # Load all schema JSON files
        self.logger.info(f"Loading {len(self.schema_files)} schema files")
        for file_name in tqdm(self.schema_files, desc="Loading schema files"):
            schema_name = file_name.split('.')[0]
            file_path = Path(self.schemas_dir) / file_name
            try:
                with open(file_path, 'r') as f:
                    self.schema_data[schema_name] = json.load(f)
                self.logger.debug(f"Loaded {file_name}")
            except Exception as e:
                self.logger.error(f"Error loading {file_path}: {str(e)}")
        
        # Create index for faster entity lookup
        # self.logger.info("Creating entity index")
        self.entity_index = {}
        for schema_name, entities in self.schema_data.items():
            for entity in entities:
                if 'id' in entity:
                    self.entity_index[entity['id']] = {
                        'schema': schema_name,
                        'entity': entity
                    }


    def load_data_from_db(self):
        """
        Loads all schema data from the database and creates an entity index.
        This function replicates the original 'load_data' logic but uses database
        functions instead of file system operations.
        """
        # 1. Load all schema data from the database
        schema_datas = get_all_jsons_for_json_type(self.document_id, JsonType.CONNECTED_SCHEMA)

        # 2. Parse and store schema data
        self.logger.info(f"Loading {len(schema_datas)} schema documents")
        for schema_json in tqdm(schema_datas, desc="Loading schemas from DB"):
            try:
                schema_name = schema_json.get('schema_name')
                self.schema_data[schema_name] = schema_json.get('json_value', [])
                self.logger.debug(f"Loaded schema '{schema_name}'")
            except Exception as e:
                self.logger.error(f"Error loading schema '{schema_name}': {str(e)}")
                
        # 3. Create index for faster entity lookup
        self.logger.info("Creating entity index")
        self.entity_index = {}
        for schema_name, entities in self.schema_data.items():
            for entity in entities:
                if 'id' in entity:
                    self.entity_index[entity['id']] = {
                        'schema': schema_name,
                        'entity': entity
                    }
    
    def get_schema_attributes_with_cardinality(self, schema_name):
        result = {}
        schema_def = self.usdm_data_dictionary[schema_name]
        for attr in schema_def['attributes']:
            cardinality = attr.get('Cardinality')
            if cardinality is not None:
                result[attr['Attribute Name']] = {
                    'data_type': attr['Data Type'],
                    'cardinality': cardinality
                }
                
        return result
    
    def get_entity_by_id(self, entity_id):
        if not isinstance(entity_id, str):
            return None, None
            
        if entity_id in self.entity_index:
            entry = self.entity_index[entity_id]
            schema_name = entry['schema']
            # Track used schema
            self.used_schemas.add(schema_name)
            return schema_name, entry['entity']
        return None, None
    
    def process_entity(self, schema_name, entity, depth=0, max_depth=15):

        if depth > max_depth:
            self.logger.warning(f"Max recursion depth reached for {schema_name} entity {entity.get('id', 'unknown')}")
            return entity
            
        # Skip if already processed to avoid circular references
        entity_id = entity.get('id')
        if entity_id:
            entity_key = f"{schema_name}:{entity_id}"
            if entity_key in self.processed_entities:
                return entity
            self.processed_entities.add(entity_key)
        
        enriched_entity = entity.copy()
        
        # Get attributes with cardinality for this schema
        attrs = self.get_schema_attributes_with_cardinality(schema_name)
        
        # Process each attribute with cardinality
        for attr_name, attr_info in attrs.items():
            if attr_name not in enriched_entity or enriched_entity[attr_name] is None:
                continue
                
            # Process based on cardinality and actual data type
            attr_value = enriched_entity[attr_name]
            
            # Handle array values
            if isinstance(attr_value, list):
                if not attr_value:  # Skip empty lists
                    continue
                    
                linked_entities = []
                for entity_id in attr_value:
                    # Skip if entity_id is not a string (can't be a reference)
                    if not isinstance(entity_id, str):
                        linked_entities.append(entity_id)
                        continue
                        
                    target_schema, target_entity = self.get_entity_by_id(entity_id)
                    if target_entity:
                        # Recursively process this entity
                        processed_entity = self.process_entity(
                            target_schema, 
                            target_entity, 
                            depth + 1, 
                            max_depth
                        )
                        linked_entities.append(processed_entity)
                    else:
                        # Keep original ID if entity not found
                        linked_entities.append(entity_id)
                
                enriched_entity[attr_name] = linked_entities
            # Handle single value (string ID)
            elif isinstance(attr_value, str):
                target_schema, target_entity = self.get_entity_by_id(attr_value)
                if target_entity:
                    # Recursively process this entity
                    processed_entity = self.process_entity(
                        target_schema, 
                        target_entity, 
                        depth + 1, 
                        max_depth
                    )
                    enriched_entity[attr_name] = processed_entity
            # Other types (int, bool, etc.) - leave as is
        
        return enriched_entity
    
    def link_study(self, study_id):
        self.processed_entities = set()  # Reset processed entities
        schema_name, study = self.get_entity_by_id(study_id)
        
        if study is None:
            self.logger.error(f"Study with ID {study_id} not found")
            return None
            
        # self.logger.info(f"Processing study {study_id}")
        return self.process_entity(schema_name, study)
    
    def run(self, study_id='Study_1'):
        self.logger.info("Starting schema linking process")
        self.load_data_from_db()
        self.unused_schemas = set(self.schema_data.keys())
        self.used_schemas = set()
        result = self.link_study(study_id)
        self.unused_schemas -= self.used_schemas
        # self.logger.info(f"Schema linking complete. Used {len(self.used_schemas)} schemas, {len(self.unused_schemas)} schemas were not used.")
        self.logger.info(f"Used schemas: {sorted(list(self.used_schemas))}")
        self.logger.info(f"Unused schemas: {sorted(list(self.unused_schemas))}")
        return result
