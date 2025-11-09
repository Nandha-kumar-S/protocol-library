from modules.document.models import JsonType
from modules.jobs.models import JobStatus
from db.database import get_db_context
from db.db_service import DBService
from modules.document.utils import get_document
from modules.jobs.utils import get_job, update_job_to_next_status
from utils.job_utils import read_json_from_db, save_json_to_db, update_stage_execution_status
from ml.scripts.pipeline.connector import SchemaConnector
from ml.scripts.pipeline.extractor import ContentExtractor
from ml.scripts.pipeline.linker import UsdmSchemaLinker
from ml.scripts.pipeline.mapper import SectionSchemaMapper
from ml.scripts.pipeline.parser import PDFParser
from ml.scripts.pipeline.preprocessor import PDFPreprocessor
from ml.scripts.pipeline.writer import USDMWriter


def parse_pdf(document_id):
    with get_db_context() as db_session:
        document = get_document(db_session, document_id)

    pdf_parser = PDFParser(document.document_url)
    markdown_file, structured_pdf = pdf_parser.parse()
    save_json_to_db(document_id=document_id, json_type=JsonType.STRUCTURED_PDF, json_value=structured_pdf, schema_name=None) # Move to backend folder so that we can import the enums
    
    extracted_text = "Extracted text from PDF"
    return {"extracted_text": extracted_text}


def preprocess_pdf(document_id):
    preprocessor = PDFPreprocessor()
    structured_pdf = read_json_from_db(document_id=document_id, json_type=JsonType.STRUCTURED_PDF)
    preprocessed_pdf = preprocessor.preprocess(structured_pdf)
    save_json_to_db(document_id=document_id, json_type=JsonType.PREPROCESSED_PDF, json_value=preprocessed_pdf)
    return preprocessed_pdf


def map_protocol_sections(document_id):
    preprocessed_pdf = read_json_from_db(document_id=document_id, json_type=JsonType.PREPROCESSED_PDF)   # TODO: We have to use preprocessed PDF here right? in main.py it is structured PDF

    section_schema_mapper = SectionSchemaMapper()
    section_schema_map = section_schema_mapper.map_sections(preprocessed_pdf)
    save_json_to_db(document_id=document_id, json_type=JsonType.SECTION_SCHEMA_MAP, json_value=section_schema_map)


def extract_content(document_id):
    preprocess_pdf = read_json_from_db(document_id=document_id, json_type=JsonType.PREPROCESSED_PDF)
    section_schema_map = read_json_from_db(document_id=document_id, json_type=JsonType.SECTION_SCHEMA_MAP)

    extracter = ContentExtractor()
    extracted_content = extracter.process_content_extraction(preprocess_pdf, section_schema_map)

    save_json_to_db(document_id=document_id, json_type=JsonType.EXTRACTED_CONTENT, json_value=extracted_content)

    return extracted_content


def map_sections_to_usdm(document_id):
    extracted_content = read_json_from_db(document_id=document_id, json_type=JsonType.EXTRACTED_CONTENT)
    usdm_writer = USDMWriter(output_dir='',document_id=document_id)

    # TODO: Have to modify the save json logic inside the function here
    usdm_writer.map_to_usdm(extracted_content)


def connect_schemas(document_id):
    # TODO: Have to implement schemas reading logic and output logic inside here
    connector = SchemaConnector(output_dir='', document_id=document_id)
    connector.connect_schemas()


def link_schemas_to_usdm(document_id):
    # TODO: Have to implement schemas reading logic inside here
    linker = UsdmSchemaLinker(output_dir='', document_id=document_id)
    final_usdm = linker.run()
    save_json_to_db(document_id=document_id, json_type=JsonType.USDM_JSON, json_value=final_usdm)


def process_document_job(job_id: int = None):
    print(f"Processing job_id {job_id}")

    with get_db_context() as db_session:
        job = get_job(db=db_session, job_id=job_id)

    print(f"Current job status: {job.status}")

    if job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CONTENT_EXTRACTION_PAUSED]:
        print(f"Job {job_id} is already in terminal state: {job.status}")
        return False

    update_stage_execution_status(job_id, "IN_PROGRESS")

    job_status_function_map = {
        JobStatus.PARSING: parse_pdf,
        JobStatus.PREPROCESSING: preprocess_pdf,
        JobStatus.MAP_SECTIONS_TO_SCHEMAS: map_protocol_sections,
        JobStatus.CONTENT_EXTRACTION: extract_content,
        JobStatus.MAP_CONTENT_TO_SCHEMAS: map_sections_to_usdm,
        JobStatus.CONNECT_SCHEMAS: connect_schemas,
        JobStatus.LINK_SCHEMAS: link_schemas_to_usdm,
    }

    fn = job_status_function_map.get(job.status)

    try:
        fn(job.document_id)
    except Exception as e:
        print(f"Error processing job {job_id} at stage {job.status}: {e}")
        update_stage_execution_status(job_id, "FAILED", error_message=str(e))
        return False

    update_stage_execution_status(job_id, "COMPLETED")

    update_job_to_next_status(job_id, job.status)
    return True


def handle_job_flows(job_id: int = None):
    try:
        while True:
            job_return = process_document_job(job_id)
            if not job_return:
                break

        return {"status": "success", "message": "Completed all job stages for document", "job_return": job_return}
    except Exception as e:
        print("Error while running job flows:", str(e))
        return {"status": "error", "message": str(e)}
        

