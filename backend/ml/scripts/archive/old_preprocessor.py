import json
import pandas as pd
import sys
import logging
from tqdm import tqdm
sys.path.insert(0, '../')
from constants.prompts import *
from ml.scripts.llm import GenAIModel
from ml.scripts.utils import get_prompt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFPreprocessor:
    def __init__(self):
        logging.info("Initialized PDFPreprocessor")
        self.ai_model = GenAIModel()

    def clean_text(self, text):
        if len(text) > 0:
            prompt = get_prompt('CleanText', text)
            cleaned_text = self.ai_model.infer(prompt).get('clean_text', '')
            return cleaned_text
        else:
            return ""
    
    def align_table_data(self, data, columns):
        col_len = len(columns)
        aligned_data = []
        for row in data:
            if len(row) < col_len:
                aligned_row = row + [""] * (col_len - len(row))
            elif len(row) > col_len:
                aligned_row = row[:col_len]
            else:
                aligned_row = row
            aligned_data.append(aligned_row)
        return aligned_data

    def clean_tables(self, tables):
        if len(tables) > 0:
            prompts = [
                get_prompt('CleanTable', pd.DataFrame(table['data'], columns=table['columns']).to_markdown(index=False))
                for table in tables
            ]
            cleaned_tables = [self.ai_model.infer(prompt)['clean_table'] for prompt in prompts]
            aligned_cleaned_tables = []
            for table in cleaned_tables:
                columns = table['columns']
                data = self.align_table_data(table['data'], columns)
                df = pd.DataFrame(data, columns=columns)
                aligned_cleaned_tables.append(df.to_markdown(index=False))
            return aligned_cleaned_tables
        else:
            return []

    def preprocess_pdf(self, structured_pdf):
        logging.info("Starting PDF preprocessing")
        for entry in tqdm(structured_pdf, desc="Preprocessing Sections and it's Subsections"):
            # logging.info(f"Processing entry: {entry.get('title', 'No Title')}")
            cleaned_text = self.clean_text(entry.get('text', ""))
            cleaned_tables = entry.get('tables', [])
            # cleaned_tables = self.clean_tables(entry.get('tables', []))

            entry['cleaned_text'] = cleaned_text
            entry['cleaned_tables'] = cleaned_tables
            
            if entry.get('subsections'):
                self.preprocess_pdf(entry['subsections'])
        logging.info("PDF preprocessing completed")
        return structured_pdf

# Example usage
if __name__ == "__main__":
    with open("structured_pdf.json", "r") as file:
        structured_pdf = json.load(file)

    preprocessor = PDFPreprocessor()
    preprocessed_pdf = preprocessor.preprocess_pdf(structured_pdf)

    with open("preprocessed_pdf.json", "w") as file:
        json.dump(preprocessed_pdf, file)