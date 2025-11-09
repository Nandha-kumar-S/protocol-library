import os
import json
import logging
import warnings
from pathlib import Path
from ml.scripts.core.config_loader import ConfigLoader
from sentence_transformers import SentenceTransformer, util

# Filter out the specific FutureWarning from PyTorch
warnings.filterwarnings("ignore", message="`encoder_attention_mask` is deprecated")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SchemaSearcher:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.logger = logging.getLogger(__name__)
        
        # Load config and USDM data dictionary
        self.config_loader = ConfigLoader()
        self.config_data = self.config_loader.get_config_data()
        self.usdm_data_dictionary = self.config_data['usdm_data_dictionary']
        
        # Initialize the sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.logger.info("Sentence transformer model loaded successfully")
    
    def get_searchable_attributes(self, schema_name):
        searchable_attributes = []
        text_related_keywords = ['description', 'name', 'text', 'title', 'condition', 
                               'role', 'summary', 'reason', 'status', 'type']
        
        if schema_name in self.usdm_data_dictionary:
            schema_def = self.usdm_data_dictionary[schema_name]
            for attribute in schema_def.get('attributes', []):
                attr_name = attribute.get('Attribute Name', '').lower()
                if any(keyword in attr_name for keyword in text_related_keywords):
                    searchable_attributes.append(attribute['Attribute Name'])
        else:
            self.logger.warning(f"Schema '{schema_name}' not found in USDM data dictionary")
        
        return searchable_attributes
    
    def semantic_similarity(self, text1, text2):
        # Ensure texts are strings
        text1 = str(text1) if text1 is not None else ""
        text2 = str(text2) if text2 is not None else ""
        
        if not text1 or not text2:
            return 0.0
        
        # Get embeddings
        embedding1 = self.model.encode(text1, convert_to_tensor=True)
        embedding2 = self.model.encode(text2, convert_to_tensor=True)
        
        # Calculate cosine similarity
        similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
        # Convert from [-1, 1] to [0, 1] range
        normalized_similarity = (similarity + 1) / 2
        return normalized_similarity
    

    
    def search_schemas(self, schema_name, search_text, similarity_threshold=0.7):
        results = []
        searchable_attributes = self.get_searchable_attributes(schema_name)
        
        if not searchable_attributes:
            self.logger.warning(f"No searchable attributes found for schema '{schema_name}'")
            return results
            
        self.logger.info(f"Searching for '{search_text}' in schema '{schema_name}'")
        # self.logger.info(f"Searchable attributes: {searchable_attributes}")
        
        # Find all protocol folders in output directory
        protocol_folders = [f for f in os.listdir(self.output_dir) 
                           if os.path.isdir(os.path.join(self.output_dir, f))]
        
        # Dictionary to track best match per protocol
        best_matches = {}
                           
        for protocol in protocol_folders:
            schema_path = os.path.join(self.output_dir, protocol, 'individual_schemas', f"{schema_name}.json")
            
            if os.path.exists(schema_path):
                self.logger.info(f"Checking protocol: {protocol}")
                try:
                    with open(schema_path, 'r') as f:
                        schema_instances = json.load(f)
                    
                    # Track best match for this protocol
                    protocol_best_score = 0
                    protocol_best_match = None
                    
                    for instance in schema_instances:
                        max_score = 0
                        matching_attribute = None
                        matching_value = None
                        
                        for attr in searchable_attributes:
                            if attr in instance:
                                attr_value = instance[attr]
                                if attr_value:
                                    similarity = self.semantic_similarity(search_text, attr_value)
                                    if similarity > max_score:
                                        max_score = similarity
                                        matching_attribute = attr
                                        matching_value = attr_value
                        
                        # If this instance has a better score than previous instances for this protocol
                        if max_score >= similarity_threshold and max_score > protocol_best_score:
                            protocol_best_score = max_score
                            protocol_best_match = {
                                'protocol': protocol,
                                'schema': schema_name,
                                'instance_id': instance.get('id', 'unknown'),
                                'matching_attribute': matching_attribute,
                                'similarity_score': max_score,
                                'attribute_value': matching_value
                            }
                    
                    # Add the best match for this protocol if one was found
                    if protocol_best_match:
                        best_matches[protocol] = protocol_best_match
                except Exception as e:
                    self.logger.error(f"Error processing {schema_path}: {e}")
        
        # Convert best_matches dictionary to a list
        results = list(best_matches.values())
        
        # Sort results by similarity score (highest first)
        results.sort(key=lambda x: x['similarity_score'], reverse=True)
        self.logger.info(f"Found {len(results)} matches with similarity >= {similarity_threshold}")
        return results

def search_protocols(schema_name, search_text, output_dir="output", similarity_threshold=0.7):
    searcher = SchemaSearcher(output_dir)
    results = searcher.search_schemas(schema_name, search_text, similarity_threshold)
    
    print(f"Found {len(results)} matches for '{search_text}' in schema '{schema_name}':")
    for i, result in enumerate(results, 1):
        print(f"{i}. Protocol: {result['protocol']}")
        print(f"   Schema: {result['schema']}")
        print(f"   Instance ID: {result['instance_id']}")
        print(f"   Matching attribute: {result['matching_attribute']}")
        print(f"   Similarity score: {result['similarity_score']:.2f}")
        
        # Truncate long attribute values for display
        attr_value = result['attribute_value']
        if isinstance(attr_value, str) and len(attr_value) > 100:
            print(f"   Value: {attr_value[:100]}...")
        else:
            print(f"   Value: {attr_value}")
        print()
    
    return results
