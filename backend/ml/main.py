import os
import json
import time
import logging

from ml.scripts.pipeline.parser import PDFParser
from ml.scripts.pipeline.preprocessor import PDFPreprocessor
from ml.scripts.pipeline.mapper import SectionSchemaMapper
from ml.scripts.pipeline.extractor import ContentExtractor
from ml.scripts.pipeline.writer import USDMWriter  
from ml.scripts.pipeline.connector import SchemaConnector
from ml.scripts.pipeline.linker import UsdmSchemaLinker


from ml.scripts.tools.search import SchemaSearcher, search_protocols
from ml.scripts.core.utils import save_json, save_markdown

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(protocol_path, output_dir):
    start_time = time.time()
    logging.info(f"Pipeline started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    '''with open("output/Alexion/section_schema_map.json", "r") as f:
        section_schema_map = json.load(f)
    with open("output/Alexion/preprocessed_pdf.json", "r") as f:
        preprocessed_pdf = json.load(f)
    with open("output/Alexion/extracted_content.json", "r") as f:
        extracted_content = json.load(f)
    with open("output/Pfizer/extracted_content.json", "r") as f:
        extracted_content = json.load(f)
    with open("output/lzzt/structured_pdf.json", "r") as f:
        structured_pdf = json.load(f)'''
    
    # Parse the PDF
    pdf_parser = PDFParser(protocol_path)
    markdown_file, structured_pdf = pdf_parser.parse()
    save_json(structured_pdf, output_dir, "structured_pdf.json")
    save_markdown(markdown_file, output_dir, "markdown.md")

    #Preprocess the structured PDF
    preprocessor = PDFPreprocessor()
    preprocessed_pdf = preprocessor.preprocess(structured_pdf)
    save_json(preprocessed_pdf, output_dir, "preprocessed_pdf.json")

    # Map protocol sections to relevant usdm schemas
    section_schema_mapper = SectionSchemaMapper()
    section_schema_map = section_schema_mapper.map_sections(preprocessed_pdf)
    save_json(section_schema_map, output_dir, "section_schema_map.json")
    
    # Content extraction
    extracter = ContentExtractor(output_dir)
    extracted_content = extracter.process_content_extraction(preprocessed_pdf, section_schema_map)
    save_json(extracted_content, output_dir, "extracted_content.json")
    
    # Map sections content to usdm schemas
    usdm_writer = USDMWriter(output_dir)
    usdm_writer.map_to_usdm(extracted_content)
    
    # Connect schemas
    connector = SchemaConnector(output_dir)
    connector.connect_schemas()

    # Link schemas to usdm network
    linker = UsdmSchemaLinker(output_dir)
    final_usdm = linker.run()
    save_json(final_usdm, output_dir, "usdm.json")

    end_time = time.time()
    total_time = end_time - start_time
    logging.info(f"Pipeline finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    logging.info(f"Total execution time: {total_time:.2f} seconds")

if __name__ == "__main__":
    
    # Process PDF to USDM
    output_dir = 'output/lzzt'
    main('input/protocol_documents/Lzzt_protocol_redacted.pdf', output_dir)
    
    # Search for Wilson Disease in the Condition schema
    #search_protocols(schema_name = 'Condition', search_text = 'the weather is like cancer',
    #                 output_dir = output_dir, similarity_threshold=0.7)