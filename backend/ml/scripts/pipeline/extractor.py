import json
import os
import sys
import logging
from tqdm import tqdm
from collections import defaultdict
sys.path.insert(0, '../')
from ml.scripts.core.llm import GenAIModel
from ml.scripts.core.utils import get_prompt
from ml.scripts.core.config_loader import ConfigLoader

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ContentExtractor:
    def __init__(self, output_dir="output/content_extraction"):
        self.ai_model = GenAIModel()
        self.config_data = ConfigLoader()
        self.config_data = self.config_data.get_config_data()
        self.usdm_data_dictionary = self.config_data.get('usdm_data_dictionary', {})
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"ContentExtractor initialized. Output directory: {self.output_dir}")
    
    def invert_section_schema_map(self, section_schema_map):
        inverted_map = defaultdict(list)
        
        for title, schemas in section_schema_map.items():
            for schema in schemas:
                inverted_map[schema].append(title)
        
        self.logger.info(f"Inverted section_schema_map: {len(inverted_map)} schemas found")
        print( dict(inverted_map))
        return dict(inverted_map)
    
    def get_schema_definition(self, schema_name):
        try:
            schema_info = self.usdm_data_dictionary.get(schema_name)
            if not schema_info:
                self.logger.warning(f"Schema '{schema_name}' not found in data dictionary")
                return None
                
            details = schema_info.get('details', {})
            return {
                'name': schema_name,
                'preferred_term': details.get('Preferred Term', 'No preferred term'),
                'definition': details.get('Definition', 'No definition provided.')
            }
        except Exception as e:
            self.logger.error(f"Failed to get schema definition for '{schema_name}': {e}")
            return None
    
    def find_content_by_title(self, preprocessed_pdf, target_title):
        for section in preprocessed_pdf:
            title = section.get('title', '')
            
            if title == target_title:
                return {
                    'title': title,
                    'cleaned_text': section.get('cleaned_text', ''),
                    'cleaned_tables': section.get('cleaned_tables', [])
                }
            
            subsections = section.get('subsections', [])
            if subsections:
                result = self.find_content_by_title(subsections, target_title)
                if result:
                    return result
        
        return None
    
    def extract_content_for_schema(self, schema_name, schema_definition, title, content_data):
        extracted_results = {'text': '', 'tables': []}
        
        try:
            cleaned_text = content_data.get('cleaned_text', '')
            extracted_results['tables']= content_data.get('cleaned_tables', [])
            
            schema_info = f"Schema: {schema_name}\nPreferred Term: {schema_definition['preferred_term']}\nDefinition: {schema_definition['definition']}"
            
            if cleaned_text and len(cleaned_text.strip()) > 50:
                protocol_content = f"Section: {title}\nContent:\n{cleaned_text}"
                input_data = f"PROTOCOL_CONTENT:\n{protocol_content}\n\nUSDM_SCHEMA:\n{schema_info}"
                
                prompt = get_prompt('TextContentExtractor', input_data)
                result = self.ai_model.infer(prompt)
                extracted_results['text'] = result.get('extracted_content', '')
                
                # self.logger.info(f"Extracted text content for schema '{schema_name}' from '{title}': {len(extracted_results['text'])} characters")
            else:
                self.logger.info(f"Skipping text extraction for schema '{schema_name}' from '{title}': text too short ({len(cleaned_text.strip())} characters)")
            
            return extracted_results
            
        except Exception as e:
            self.logger.error(f"Failed to extract content for schema '{schema_name}' from '{title}': {e}")
            return {'text': '', 'tables': []}
    
    def process_content_extraction(self, preprocessed_pdf, section_schema_map):

        self.logger.info("Starting content extraction process...")
        
        # Step 1: Invert the section_schema_map
        inverted_map = self.invert_section_schema_map(section_schema_map)
        
        # Step 2: Process each schema
        extracted_content = {}
        
        for schema_name, titles in tqdm(inverted_map.items(), desc="Processing schemas"):
            # self.logger.info(f"Processing schema: {schema_name}")
            
            # Step 3: Check if schema exists in USDM data dictionary
            schema_definition = self.get_schema_definition(schema_name)
            if not schema_definition:
                self.logger.warning(f"Skipping schema '{schema_name}' - not found in data dictionary")
                continue
            
            # Initialize schema results
            if schema_name not in extracted_content:
                extracted_content[schema_name] = []
            
            # Step 4: Process each title separately (make separate calls for each entry)
            for title in titles:
                # self.logger.info(f"Processing title '{title}' for schema '{schema_name}'")
                
                # Step 5: Find content from preprocessed_pdf for this specific title
                content_data = self.find_content_by_title(preprocessed_pdf, title)
                
                if not content_data:
                    self.logger.warning(f"No content found for schema '{schema_name}' with title: '{title}'")
                    continue
                
                # Step 6: Extract relevant content using AI model (separate calls)
                extracted_results = self.extract_content_for_schema(schema_name, schema_definition, title, content_data)
                
                # Step 7: Store the extracted content if any content was found
                if extracted_results['text'] or extracted_results['tables']:
                    result_entry = {
                        'title': title,
                        'extracted_text': extracted_results['text'],
                        'extracted_tables': extracted_results['tables']
                    }
                    extracted_content[schema_name].append(result_entry)
                    # self.logger.info(f"Added extracted content for schema '{schema_name}' from title '{title}'")
        
        # self.logger.info(f"Content extraction completed. Processed {len(extracted_content)} schemas")

        # Final step: Ensure essential schemas are present
        if 'Study' in extracted_content and extracted_content['Study']:
            study_content = extracted_content['Study']
            if 'StudyVersion' not in extracted_content or not extracted_content['StudyVersion']:
                extracted_content['StudyVersion'] = study_content
            if 'StudyDefinitionDocument' not in extracted_content or not extracted_content['StudyDefinitionDocument']:
                extracted_content['StudyDefinitionDocument'] = study_content
        else:
            self.logger.warning("Could not enforce essential schemas because 'Study' content is missing.")

        return extracted_content
