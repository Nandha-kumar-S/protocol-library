
from fastapi import HTTPException
from db.database import get_db_context
from modules.jobs import models, schemas
from sqlalchemy.orm import Session

def get_job(db: Session, job_id: int) -> schemas.JobResponse:
    """
    Get job by ID
    """
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    return schemas.JobResponse.from_orm(job)



def update_job_to_next_status(job_id: int, current_status: models.JobStatus|str) -> None:
    """
    Update job to the next status in the workflow
    """
    with get_db_context() as db:
        job = db.query(models.Job).filter(models.Job.id == job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        
        status_flow = [
            models.JobStatus.STARTED,
            models.JobStatus.PARSING,
            models.JobStatus.PREPROCESSING,
            models.JobStatus.MAP_SECTIONS_TO_SCHEMAS,
            models.JobStatus.CONTENT_EXTRACTION,
            models.JobStatus.CONTENT_EXTRACTION_PAUSED,
            models.JobStatus.MAP_CONTENT_TO_SCHEMAS,
            models.JobStatus.CONNECT_SCHEMAS,
            models.JobStatus.LINK_SCHEMAS,
            models.JobStatus.COMPLETED
        ]
        
        try:
            current_index = status_flow.index(models.JobStatus[current_status.value])
            if current_index + 1 < len(status_flow):
                job.status = status_flow[current_index + 1]
                job.current_stage_execution_status = models.CurrentStageExecutionStatus.NOT_STARTED.value
                db.commit()
                db.refresh(job)
                print(f"Job {job_id} status updated to {job.status}")
        except KeyError as e:
            raise Exception(f"Invalid current status {current_status}. {status_flow=}")
        
        except Exception as e:
            raise Exception(f"Error updating job status: {str(e)}")
