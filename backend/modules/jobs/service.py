from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from typing import List, Optional, Dict
from ml.stages.processors import handle_job_flows
from db.database import get_db_context
from utils.job_utils import update_stage_execution_status
from modules.jobs import models, schemas
from modules.document.models import Document
from utils.utils import run_in_background
from fastapi import BackgroundTasks


async def get_dashboard_status(db: Session) -> dict:
    """
    Get count of jobs grouped by status for dashboard
    """
    counts = db.query(
        models.Job.status,
        func.count(models.Job.id)
    ).group_by(models.Job.status).all()
    
    return {status.name: count for status, count in counts}

def get_jobs(
    db: Session,
    document_name: Optional[str] = None,
    status: Optional[str] = None
) -> List[schemas.JobResponse]:
    """
    Get all jobs with optional filters for document name and status
    """
    query = db.query(models.Job).join(Document)
    
    if status:
        try:
            job_status = models.JobStatus[status.upper()]
            query = query.filter(models.Job.status == job_status)
        except KeyError:
            raise HTTPException(status_code=400, detail="Invalid status")
    
    if document_name:
        query = query.filter(Document.filename.ilike(f"%{document_name}%"))
    
    jobs = query.all()
    return [schemas.JobResponse.from_orm(job) for job in jobs]


def update_job_status(db: Session, job_id: int, action: str, background_tasks: BackgroundTasks) -> schemas.JobResponse:
    """
    Update job status based on approval/rejection
    """
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Status transition logic
    status_transitions = {
        "APPROVE": {
            models.JobStatus.CONTENT_EXTRACTION_PAUSED: models.JobStatus.MAP_CONTENT_TO_SCHEMAS,
        },
        "REJECT": {
            models.JobStatus.CONTENT_EXTRACTION_PAUSED: models.JobStatus.FAILED,
        }
    }
    
    if action in status_transitions and job.status in status_transitions[action]:
        job.status = status_transitions[action][job.status]
        if action == "REJECT":
            update_stage_execution_status(job_id, models.CurrentStageExecutionStatus.NOT_STARTED, error_message="Job rejected by user")

        update_stage_execution_status(job_id, models.CurrentStageExecutionStatus.NOT_STARTED)
        db.commit()
        db.refresh(job)

        run_in_background(background_tasks, handle_job_flows, job.id)

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status for transition with action '{action}'"
        )
    
    return schemas.JobResponse.from_orm(job)

def create_job(db: Session, document_id) -> schemas.JobResponse:
    """
    Create a new job
    """
    db_job = models.Job(
        document_id=document_id,
        status=models.JobStatus.PARSING
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    
    return schemas.JobResponse.from_orm(db_job)
