from utils.job_utils import get_all_jsons_for_json_type, read_json_from_db, save_json_to_db
from ml.constants.prompts import *
import json
import os
import logging
from pathlib import Path
from tqdm import tqdm
from ml.scripts.core.config_loader import ConfigLoader
from ml.constants.prompts import *
from ml.scripts.core.llm import GenAIModel
from ml.scripts.core.utils import get_prompt
from modules.document.models import JsonType

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SchemaConnector:
    def __init__(self, output_dir, document_id):
        self.ai_model = GenAIModel()
        self.config_loader = ConfigLoader()
        self.config_data = self.config_loader.get_config_data()
        self.usdm_data_dictionary = self.config_data['usdm_data_dictionary']
        self.schemas_dir = os.path.join(output_dir, 'individual_schemas')
        self.output_dir = output_dir
        self.json_type = JsonType.CONNECTED_SCHEMA
        self.document_id = document_id
        
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"SchemaConnector initialized. Output directory: {self.output_dir}")
    
        # Fetch the individual schemas from the database
        self.all_schemas_dict = self.read_json_files_from_db(document_id=document_id, json_type=JsonType.INDIVIDUAL_SCHEMA)  # TODO: document_id should be passed as argument to constructor


    def read_json_files(self, path):
        schemas_dict = {}
        json_files = list(Path(path).glob('*.json'))
        
        for file in tqdm(json_files, desc="Loading schema files"):
            file_name = file.name
            try:
                with file.open('r') as f:
                    json_data = json.load(f)
                    if json_data:
                        schemas_dict[file_name.split('.')[0]] = json_data
            except Exception as e:
                self.logger.error(f"Unexpected error reading {file}: {e}")
        return schemas_dict
    
    def read_json_files_from_db(self, document_id, json_type):
        jsons = get_all_jsons_for_json_type(document_id=document_id, json_type=json_type)
        schemas_dict = {}
        for json_entry in jsons:
            schema_name = json_entry.get('schema_name')
            json_value = json_entry.get('json_value')
            if schema_name and json_value:
                schemas_dict[schema_name] = json_value
        return schemas_dict

    def get_child_schemas(self, schema_name):
        child_schemas = []
        for schema in self.usdm_data_dictionary:
            if schema == schema_name:
                for attribute in self.usdm_data_dictionary[schema]['attributes']:
                    if attribute['Cardinality'] is not None:
                        child_schemas.append(attribute['Data Type'])
        return child_schemas

    def format_schema_data(self, schema_name, schema_data):
        formatted_schema_data = f"{schema_name}\n"
        for entry in schema_data:
            for attribute, value in entry.items():
                formatted_schema_data += f"  {attribute}: {value}\n"
            formatted_schema_data += "\n"
        return formatted_schema_data

    def get_target_attribute_data(self, parent_schema_name, child_schema_name):
        target_attributes = []
        try:
            for schema in self.usdm_data_dictionary:
                if schema == parent_schema_name:
                    for attribute in self.usdm_data_dictionary[schema]['attributes']:
                        if attribute['Data Type'] == child_schema_name:
                            target_attributes.append(attribute)
        except Exception as e:
            self.logger.error(f"Unexpected error in get_target_attribute_data: {e}")
        return target_attributes
    
    def insert_to_usdm(self, usdm_data):
        for key, value in tqdm(usdm_data.items(), desc="Saving USDM data"):
            file_path = os.path.join(self.output_dir, 'connected_schemas', f"{key}.json")
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            existing_data = []
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        existing_data = json.load(f)
                    except json.JSONDecodeError:
                        self.logger.warning(f"Could not decode JSON from {file_path}. Starting fresh.")
                        existing_data = []

            if isinstance(value, list):
                existing_data.extend(value)
            else:
                existing_data.append(value)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
                self.logger.debug(f"Wrote data to {file_path}")

    def insert_usdm_data_to_db(self, usdm_data):
        for key, value in tqdm(usdm_data.items(), desc="Saving USDM data to DB"):
            json_type = self.json_type
            schema_name = key

            # 1. Read existing data from the DB
            existing_data = read_json_from_db(self.document_id, json_type, schema_name)
            if not existing_data:
                existing_data = []

            # 2. Append new data to existing data
            if isinstance(value, list):
                existing_data.extend(value)
            else:
                existing_data.append(value)
            
            # 3. Save the combined data back to the DB
            response = save_json_to_db(self.document_id, json_type, existing_data, schema_name)
            if response:
                self.logger.debug(f"Wrote data for schema '{key}' to the database.")
            else:
                self.logger.warning(f"Failed to write data for schema '{key}' to the database.")


    def connect_schemas(self):
        try:
            parent_schemas = list(self.all_schemas_dict.items())
            # self.logger.info(f"Starting schema connection process for {len(parent_schemas)} schemas")
            
            for parent_schema_name, parent_schema_data in tqdm(parent_schemas, desc="Processing parent schemas"):
                formatted_parent_schema_data = self.format_schema_data(parent_schema_name, parent_schema_data)   
                child_schemas = self.get_child_schemas(parent_schema_name)
                
                if not child_schemas:
                    # self.logger.info(f"No child schemas found for {parent_schema_name}")
                    continue
                
                for child_schema_name in child_schemas:
                    try:
                        if child_schema_name in self.all_schemas_dict:
                            child_schema_data = self.all_schemas_dict[child_schema_name]
                            formatted_child_schema_data = self.format_schema_data(child_schema_name, child_schema_data)
                            target_attribute_datas = self.get_target_attribute_data(parent_schema_name, child_schema_name)
                            for target_attribute_data in target_attribute_datas:
                                input_data = f"""META DATA:
PARENT SCHEMA NAME: {parent_schema_name}
    TARGET ATTRIBUTE NAME: {target_attribute_data['Attribute Name']}
    TARGET ATTRIBUTE DEFINITION: {target_attribute_data['Definition']}
    TARGET ATTRIBUTE CARDINALITY: {target_attribute_data['Cardinality']}
CHILD SCHEMA NAME: {child_schema_name}

PARENT SCHEMA ENTRIES:
{formatted_parent_schema_data}
CHILD SCHEMA ENTRIES:
{formatted_child_schema_data}"""
                            
                                try:
                                    prompt = get_prompt('SchemaConnector', input_data)
                                    response = self.ai_model.infer(prompt)
                                        
                                    # Update parent schema entries with linked child IDs
                                    links_created = 0
                                    for parent_schema_entry_id, child_schema_entry_ids in response.items():
                                        for parent_schema_entry in parent_schema_data:
                                            if parent_schema_entry['id'] == parent_schema_entry_id:
                                                parent_schema_entry[target_attribute_data['Attribute Name']] = child_schema_entry_ids
                                                if child_schema_entry_ids:  # Count non-empty links
                                                    links_created += len(child_schema_entry_ids) if isinstance(child_schema_entry_ids, list) else 1
                                                break
                                                
                                    # self.logger.info(f"Successfully linked {parent_schema_name} -> {child_schema_name} for Attribute: {target_attribute_data['Attribute Name']}: {links_created} connections created")
                                    
                                except Exception as e:
                                    self.logger.error(f"Error during AI inference for {parent_schema_name} -> {child_schema_name}: {e}")
                                    continue
                        else:
                            pass  # Child schema not found - skip silently
                                
                    except Exception as e:
                        self.logger.error(f"Error processing child schema {child_schema_name}: {e}")
                        continue
                        
            self.insert_usdm_data_to_db(self.all_schemas_dict)
            # self.logger.info("Schema connection process completed successfully")
            
        except Exception as e:
            self.logger.error(f"Fatal error in connect_schemas: {e}")
            raise