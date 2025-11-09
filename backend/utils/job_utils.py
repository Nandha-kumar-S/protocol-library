from modules.document import models
from modules.jobs.models import Job
from db.database import get_db_context
from modules.document.utils import get_document_json, update_document_json


def save_json_to_db(document_id, json_type, json_value, schema_name=None):
    with get_db_context() as db:
        # NOTE: Here we set use_reviewed_json to False because this function is used in ML stages where we want to create or update the original json_type, not the reviewed version.
        response = update_document_json(db=db, document_id=document_id, json_type=json_type, json_value=json_value, schema_name=schema_name, use_reviewed_json=False)
    return response


def read_json_from_db(document_id, json_type, schema_name=None):
    with get_db_context() as db:
        json_value = get_document_json(db=db, document_id=document_id, json_type=json_type, schema_name=schema_name)
    return json_value.get('json_value')


def get_all_jsons_for_json_type(document_id, json_type):
    """
    Used to get all JSON entries for a specific document and JSON type.
    Currently used to get all individual schemas or connected schemas for a document as they have multiple entries with different schema names
    """
    # TODO: Here it must select the reviewed_json_type if exists, otherwise the original json_type
    # Currently we won't be reviewing the individual or connected scheams json type, so we won't have the respoective reviewed_json_type for now
    with get_db_context() as db:
        json_entries = db.query(models.JsonValues).filter(
            models.JsonValues.document_id == document_id,
            models.JsonValues.json_type == json_type,
            models.JsonValues.is_deleted == False
        ).all()
        
        return [json_entry.to_dict() for json_entry in json_entries]


def update_stage_execution_status(job_id, status, error_message=None):
    with get_db_context() as db:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            raise ValueError(f"Job with ID {job_id} not found")
        
        job.current_stage_execution_status = status
        if error_message:
            job.error_message = error_message

        db.commit()
        db.refresh(job)

