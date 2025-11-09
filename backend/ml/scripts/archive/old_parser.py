import fitz  # PyMuPDF
import json
import pdfplumber
import pandas as pd
import pdfplumber
from pdf2image import convert_from_path
from io import BytesIO
import sys
import logging
import re
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from ml.constants.prompts import *
from ml.scripts.llm import GenAIModel
from ml.scripts.utils import get_prompt

class PDFParser:
    def __init__(self, pdf_path):
        self.ai_model = GenAIModel()
        self.pdf_path = pdf_path
        self.sections = []
        self.pdf_text = ""
        self.tables_by_page = []
        logging.info(f"Initialized PDFParser for {pdf_path}")

    def extract_sections(self):
        logging.info("Extracting sections from PDF")
        doc = fitz.open(self.pdf_path)
        toc = doc.get_toc()
        if not toc:
            logging.warning("No table of contents found in PDF")
            doc.close()
            return []

        result = []
        stack = []

        for entry in toc:
            level, title, page = entry[0], entry[1], entry[2]
            node = {
                "title": title.strip(),
                "page": page,
                "subsections": []
            }
            while stack and stack[-1][0] >= level:
                stack.pop()
            if stack:
                stack[-1][1]["subsections"].append(node)
            else:
                result.append(node)
            stack.append((level, node))
        doc.close()
        self.sections = result
        logging.info("Sections extracted successfully")

    def extract_text(self):
        logging.info("Extracting text from PDF")
        doc = fitz.open(self.pdf_path)
        all_text = []
        for page_num in tqdm(range(doc.page_count), desc="Extracting Text"):
            page = doc.load_page(page_num)
            all_text.append(page.get_text())
        doc.close()
        self.pdf_text = "\n".join(all_text)
        # print(self.pdf_text)
        logging.info("Text extraction completed")

    def map_titles_to_text(self):
        logging.info("Mapping titles to text")
        def flatten_titles(pdf_sections):
            titles = []
            for entry in pdf_sections:
                titles.append(entry['title'])
                if entry.get('subsections'):
                    titles.extend(flatten_titles(entry['subsections']))
            return titles

        def extract_section_number(title):
            match = re.match(r'^(\d+(\.\d+)*)\.\s', title)
            if match:
                return match.group(0).strip()
            return None

        def extract_section_text(title):
            match = re.match(r'^(\d+(\.\d+)*)\.\s+(.*)', title)
            if match:
                return match.group(3).strip()
            return None 

        def find_title_position(pdf_text, title):
            # Try to find the full title first
            pos = pdf_text.rfind(title)
            if pos != -1:
                return pos
                
            # Try to find section number and section text separately
            section_number = extract_section_number(title)
            section_text = extract_section_text(title)
            
            if section_number and section_text:
                # Use regex to find section number followed by section text with any whitespace in between
                # Escape special regex characters in section_number and section_text
                escaped_section_number = re.escape(section_number)
                
                # Create pattern that matches section number, followed by any whitespace, followed by section text
                # with flexible whitespace between words in section text
                if section_text:
                    # Split the section text into words and escape each word
                    words = [re.escape(word) for word in section_text.split()]
                    # Create pattern with flexible whitespace between words
                    section_text_pattern = r'\s+'.join(words)
                    # Complete pattern with section number
                    pattern = f"{escaped_section_number}\\s*{section_text_pattern}"
                    
                    # Search for the last occurrence of this pattern (case sensitive)
                    matches = list(re.finditer(pattern, pdf_text))
                    if matches:
                        # Return the position of the last match
                        return matches[-1].start()
                
                # If still not found, try just the section number
                pos = pdf_text.rfind(section_number)
                if pos != -1:
                    return pos
                    
                # Last resort: try just the section text with flexible whitespace
                if section_text:
                    words = [re.escape(word) for word in section_text.split()]
                    section_text_pattern = r'\s+'.join(words)
                    
                    matches = list(re.finditer(section_text_pattern, pdf_text))
                    if matches:
                        return matches[-1].start()
            
            # Not found
            return -1

        def extract_title_text_chunks(pdf_text, titles):
            threshold_idx_length = 1000
            chunks = {}
            for i, title in enumerate(titles):
                # print('** ', title)
                start_idx = find_title_position(pdf_text, title)
                
                if start_idx == -1:
                    chunks[title] = ""
                    continue
                    
                start_idx += len(title)

                if i + 1 < len(titles):
                    next_idx = find_title_position(pdf_text, titles[i + 1])
                    
                    if next_idx != -1:
                        chunk = pdf_text[start_idx:next_idx]
                    else:
                        chunk = pdf_text[start_idx:start_idx + threshold_idx_length]
                else:
                    chunk = pdf_text[start_idx:start_idx + threshold_idx_length]
                chunks[title] = chunk.strip()
            return chunks

        def assign_text_to_sections(pdf_sections, title_text_dict):
            for entry in pdf_sections:
                entry['text'] = title_text_dict.get(entry['title'], "")
                if entry.get('subsections'):
                    assign_text_to_sections(entry['subsections'], title_text_dict)
            return pdf_sections

        titles = flatten_titles(self.sections)
        title_text_dict = extract_title_text_chunks(self.pdf_text, titles)
        self.sections = assign_text_to_sections(self.sections, title_text_dict)
        logging.info("Titles mapped to text successfully")

    def extract_tables(self):
        logging.info("Extracting tables from PDF")
        result = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(tqdm(pdf.pages, desc="Extracting Tables")):
                tables = page.extract_tables()
                tables_json = []
                for table in tables:
                    df = pd.DataFrame(table)
                    table_json = {
                        "columns": list(df.columns),
                        "data": df.values.tolist()
                    }
                    tables_json.append(table_json)
                if tables_json:
                    result.append({
                        "page": i + 1,
                        "tables": tables_json
                    })
        self.tables_by_page = result
        logging.info("Tables extracted successfully")

    def extract_tables_from_image(self):
        try:
            pages_with_tables = []
            with pdfplumber.open(self.pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    tables = page.extract_tables()
                    if tables:
                        pages_with_tables.append(page_num)
            
            results = []
            images = convert_from_path(self.pdf_path)
            prompt = get_prompt('ExtractTableFromImage')
            for page_num in pages_with_tables:
                if page_num in [32, 40]:
                    
                    image = images[page_num - 1]
                    img_byte_array = BytesIO()
                    image.save(img_byte_array, format='PNG')
                    image_data = img_byte_array.getvalue()
                    # print(prompt)
                    extracted_tables = self.ai_model.infer(prompt, image_data)
                    for tab in extracted_tables['tables']:
                        print(tab)
                        print('*', 20)
                    results.append({
                        "page": page_num,
                        "tables": extracted_tables['tables']
                    })
            
        except Exception as e:
            logging.error(f"An error occurred while processing the PDF: {e}")
            self.tables_by_page = []

        self.tables_by_page = results

    def map_tables_to_sections(self):
        logging.info("Mapping tables to sections")
        def flatten_sections(sections):
            flat = []
            for entry in sections:
                flat.append(entry)
                if entry.get('subsections'):
                    flat.extend(flatten_sections(entry['subsections']))
            return flat

        flat_sections = flatten_sections(self.sections)
        page_to_section = {entry['page']: entry for entry in flat_sections}
        section_pages = sorted(page_to_section.keys())

        for entry in flat_sections:
            entry['tables'] = []

        total_tables = 0
        exact_matches = 0
        nearest_matches = 0

        for table_entry in self.tables_by_page:
            table_page = table_entry['page']
            total_tables += len(table_entry['tables'])
            if table_page in page_to_section:
                page_to_section[table_page]['tables'].extend(table_entry['tables'])
                exact_matches += len(table_entry['tables'])
            else:
                nearest_page = min(section_pages, key=lambda x: abs(x - table_page))
                page_to_section[nearest_page]['tables'].extend(table_entry['tables'])
                nearest_matches += len(table_entry['tables'])

        logging.info(f"Total tables processed: {total_tables}")
        logging.info(f"Tables mapped by exact page: {exact_matches}")
        logging.info(f"Tables mapped to nearest section: {nearest_matches}")

        return self.sections        

    def parse_pdf(self):
        logging.info("Starting PDF parsing process")
        self.extract_sections()
        self.extract_text()
        self.map_titles_to_text()
        # self.extract_tables()
        self.extract_tables_from_image()
        self.map_tables_to_sections()
        logging.info("PDF parsing process completed")
        return self.sections
