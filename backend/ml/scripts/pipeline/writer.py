from utils.job_utils import read_json_from_db, save_json_to_db
from ml.constants.prompts import *
import os
from pydoc import text
import pandas as pd
import json
import logging
from tqdm import tqdm
from ml.scripts.core.config_loader import ConfigLoader
from ml.scripts.core.llm import GenAIModel
from ml.scripts.core.utils import get_prompt
from modules.document.models import JsonType

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class USDMWriter:
    def __init__(self, output_dir, document_id):
        self.ai_model = GenAIModel()
        self.config_loader = ConfigLoader()
        self.config_data = self.config_loader.get_config_data()
        self.usdm_data_dictionary = self.config_data['usdm_data_dictionary']
        self.output_dir = output_dir
        self.document_id = document_id
        self.json_type = JsonType.INDIVIDUAL_SCHEMA
        # os.makedirs(self.output_dir, exist_ok=True)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"UsdmWriter initialized")
    
    def format_usdm_schema(self, schema):
        try:
            output = []
            schema_info = self.usdm_data_dictionary.get(schema)
            if not schema_info:
                self.logger.warning(f"Schema '{schema}' not found in data dictionary.")
                output.append(f"Schema Name: {schema}\n  [No information found]\n")

            details = schema_info.get('details', {})
            preferred_term = details.get('Preferred Term', 'No preferred term')
            definition = details.get('Definition', 'No definition provided.')
            output.append(f"Schema Name: {schema}")
            output.append(f"  Preferred Term: {preferred_term.replace('\n', ' ').replace('  ', ' ').strip()}")
            output.append(f"  Definition: {definition.replace('\n', ' ').replace('  ', ' ').strip()}")

            attributes = schema_info.get('attributes', [])
            if attributes:
                output.append("  Attributes:")
                for attr in attributes:
                    if attr['Cardinality'] == None:
                        attr_name = attr.get('Attribute Name', 'Unnamed')
                        attr_type = attr.get('Data Type', '')
                        attr_def = attr.get('Definition', '')
                        output.append(f"    - {attr_name}")
                        output.append(f"\t\tData type: {attr_type}")
                        if attr_def:
                            output.append(f"\t\tDefinition: {attr_def}")
                        else:
                            output.append(f"\t\tDefinition: [No definition]")
            else:
                output.append("  [No attributes listed]")
            output.append("")
            return "\n".join(output)
        except Exception as e:
            self.logger.error(f"Failed to format schema '{schema}': {e}")
            return ""
    
    def insert_to_usdm(self, usdm_data):
        for key, value in usdm_data.items():
            if key in self.usdm_data_dictionary:
                file_path = os.path.join(self.output_dir, 'individual_schemas', f"{key}.json")
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                existing_data = []
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as f:
                        try:
                            existing_data = json.load(f)
                        except json.JSONDecodeError:
                            self.logger.warning(f"Could not decode JSON from {file_path}. Starting fresh.")
                            existing_data = []

                # Determine the starting index for new IDs
                start_index = len(existing_data)

                # Process new value(s), ensuring each gets a unique ID
                new_entries = value if isinstance(value, list) else [value]
                for idx, entry in enumerate(new_entries):
                    entry['id'] = f"{key}_{start_index + idx + 1}"
                    existing_data.append(entry)

                # TODO: Move this to DB here
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(existing_data, f, indent=2, ensure_ascii=False)
                    self.logger.debug(f"Wrote data to {file_path}")

    def append_usdm_data_to_db(self, usdm_data: dict):
        """
        Inserts data from a dictionary into the database, retaining the original logic
        of reading, appending, and writing, but using the provided DB functions.
        usdm_data_dictionary = config dictionary to identify valid schema names
        """
        for key, value in usdm_data.items():
            if key not in self.usdm_data_dictionary:
                continue

            schema_name = key

            # 1. Read existing data from the DB
            existing_data = read_json_from_db(self.document_id, self.json_type, schema_name)
            if not existing_data:
                existing_data = []

            # 2. Determine the starting index for new IDs
            start_index = len(existing_data)

            # 3. Process new value(s), ensuring each gets a unique ID
            new_entries = value if isinstance(value, list) else [value]
            for idx, entry in enumerate(new_entries):
                # Ensure a mutable copy is used if the original data should not be altered
                entry_to_save = entry.copy()
                entry_to_save['id'] = f"{key}_{start_index + idx + 1}"
                existing_data.append(entry_to_save)

            # 4. Save the combined data back to the DB
            response = save_json_to_db(self.document_id, self.json_type, existing_data, schema_name)
            if response:
                print(f"Wrote data for schema '{key}' to the database.")
            else:
                print(f"Failed to write data for schema '{key}' to the database.")


    def get_utility_schemas(self, schema):
        utility_schemas = set()
        schemas_to_process = [schema]
        while schemas_to_process:
            current_schema = schemas_to_process.pop()
            # print(current_schema)
            for attribute in self.usdm_data_dictionary.get(current_schema, {}).get('attributes', []):
                if attribute['Cardinality'] == None:
                    utility_schema = attribute['Data Type']
                    if utility_schema in self.usdm_data_dictionary and utility_schema not in utility_schemas:
                        utility_schemas.add(utility_schema)
                        schemas_to_process.append(utility_schema)

        if not utility_schemas:
            return ""

        utility_input_parts = ['\nUTILITY SCHEMAS: \n']
        utility_schema_input = [self.format_usdm_schema(utility_schema) for utility_schema in utility_schemas]
        utility_input_parts.append("".join(utility_schema_input))
        return "\n".join(utility_input_parts)

    def _process_entry_input_text(self, contents, schema):
        for content in contents:
            title = content.get('title')
            text = content.get('extracted_text')
            if len(text) > 0:
                input_parts = [f'PROTOCOL_CONTENT: \n{title}\n']
                input_parts.append(f'\n\t{text}\n')
                input_parts.append('\nUSDM_SCHEMA: \n')
                schema_input = self.format_usdm_schema(schema)
                input_parts.append(schema_input)
                utility_schemas = self.get_utility_schemas(schema)
                input_parts.append(utility_schemas)
                return "".join(input_parts)
        return None

    def _process_entry_input_tables(self, contents, schema):
        for content in contents:
            title = content.get('title')
            tables = content.get('extracted_tables')
            if len(tables) > 0:
                input_parts = [f'PROTOCOL_CONTENT: \n{title}\n']
                input_parts.append('\nTables:\n')
                for table in tables:
                    markdown_table = pd.DataFrame(table['data'], columns=table['columns']).to_markdown(index=False)
                    input_parts.append(f'\n{markdown_table}\n\n')
                input_parts.append('\nUSDM_SCHEMA: \n')
                schema_input = self.format_usdm_schema(schema)
                input_parts.append(schema_input)
                utility_schemas = self.get_utility_schemas(schema)
                input_parts.append(utility_schemas)
                return "".join(input_parts)
        return None
    
    def map_to_usdm(self, extracted_content):
        self.logger.info("Starting USDM mapping process...")
        all_usdm_data = {}
        for schema, contents in tqdm(extracted_content.items(), desc="Mapping to USDM"):
            text_input_data = self._process_entry_input_text(contents, schema)
            tables_input_data = self._process_entry_input_tables(contents, schema)
            if text_input_data is not None:
                text_prompt = get_prompt('UsdmWriter', text_input_data)
                # print(text_prompt)
                # print('*'*10)
                try:
                    text_inferred_data = self.ai_model.infer(text_prompt)
                    # print(text_inferred_data)
                    self.append_usdm_data_to_db(text_inferred_data)
                except Exception as e:
                    self.logger.error(f"Text AI inference failed for section '{schema}': {e}")
            if tables_input_data is not None:
                tables_prompt = get_prompt('UsdmWriter', tables_input_data)
                # print(tables_prompt)
                # print('*'*10)
                try:
                    tables_inferred_data = self.ai_model.infer(tables_prompt)
                    # print(tables_inferred_data)
                    self.append_usdm_data_to_db(tables_inferred_data)
                except Exception as e:
                    self.logger.error(f"Tables AI inference failed for section '{schema}': {e}")
        self.logger.info("USDM mapping process completed.")
