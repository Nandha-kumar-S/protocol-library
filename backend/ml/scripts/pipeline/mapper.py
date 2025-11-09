from ml.constants.prompts import *
import pandas as pd
from tqdm import tqdm
import logging
from ml.scripts.core.config_loader import ConfigLoader
from ml.scripts.core.utils import get_prompt
from ml.scripts.core.llm import GenAIModel

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SectionSchemaMapper:
    def __init__(self):
        logging.info("Initialized SectionSchemaMapper")
        self.ai_model = GenAIModel()
        self.config_loader = ConfigLoader()
        self.config_data = self.config_loader.get_config_data()
        self.usdm_data_dictionary = self.config_data['usdm_data_dictionary']
        self.formatted_schemas = self.format_schemas(self.usdm_data_dictionary)

    def format_schemas(self, data):
        output_lines = []
        for schema, content in data.items():
            output_lines.append(f"Schema: {schema}")
            output_lines.append(f"  Definition: {content.get('details').get('Definition', '')}")
        return "\n".join(output_lines)

    def _count_sections(self, sections):
        count = len(sections)
        for section in sections:
            if 'subsections' in section:
                count += self._count_sections(section['subsections'])
        return count

    def map_sections(self, preprocessed_pdf):
        total_sections = self._count_sections(preprocessed_pdf)
        with tqdm(total=total_sections, desc="Mapping Protocol Sections to Schemas") as pbar:
            return self._recursive_map(preprocessed_pdf, pbar)

    def _recursive_map(self, sections, pbar):
        mapped_sections_schema_dict = {}
        for entry in sections:
            title = entry['title']
            text = entry.get('cleaned_text', '')
            tables = entry.get('cleaned_tables', [])
            
            all_relevant_schemas = []

            # Make a separate call for the text content if it exists
            if text:
                text_input = f"Schemas and it's definition:\n{self.formatted_schemas}\n{"-"*20}\nCustom section: {title}\nContent:\n{text[:2000]}\n"
                prompt = get_prompt('SectionSchemaMapper', {'INPUT_DATA': text_input})
                schemas_from_text = self.ai_model.infer(prompt)
                if schemas_from_text and 'relevant_schemas' in schemas_from_text:
                    all_relevant_schemas.extend(schemas_from_text['relevant_schemas'])

            # Make a separate call for each table
            for i, table_data in enumerate(tables):
                try:
                    df = pd.DataFrame(data=table_data['data'], columns=table_data['columns'])
                    table_input = f"Schemas and it's definition:\n{self.formatted_schemas}\n{"-"*20}\nCustom section: {title}\nTable Content:\n{df.to_markdown()}\n"
                    prompt = get_prompt('SectionSchemaMapper', {'INPUT_DATA': table_input})
                    schemas_from_table = self.ai_model.infer(prompt)
                    if schemas_from_table and 'relevant_schemas' in schemas_from_table:
                        all_relevant_schemas.extend(schemas_from_table['relevant_schemas'])
                except Exception as e:
                    logging.error(f"Could not process table {i} in section '{title}'. Error: {e}")

            # Store the unique list of schemas for the section title
            if all_relevant_schemas:
                mapped_sections_schema_dict[title] = sorted(list(set(all_relevant_schemas)))

            pbar.update(1)

            # Recursively process subsections
            if entry.get('subsections'):
                sub_mappings = self._recursive_map(entry['subsections'], pbar)
                mapped_sections_schema_dict.update(sub_mappings)
                
        return mapped_sections_schema_dict
