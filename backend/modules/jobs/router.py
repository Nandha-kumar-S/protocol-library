from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from modules.jobs import service, schemas
from modules.jobs import utils
from db.database import get_db
from fastapi import BackgroundTasks


router = APIRouter(tags=["jobs"])

@router.get("/dashboard/status")
async def get_dashboard_status(
    db: Session = Depends(get_db)
) -> dict:
    """
    Get count of jobs grouped by status for dashboard
    """
    return await service.get_dashboard_status(db)

@router.get("/")
async def list_jobs(
    document_name: Optional[str] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
) -> List[schemas.JobResponse]:
    """
    Get all jobs with optional filters for document name and status.
    Frontend can poll this endpoint to get current status.
    """
    return service.get_jobs(db, document_name=document_name, status=status)

@router.get("/{job_id}")
async def get_job(
    job_id: int,
    db: Session = Depends(get_db)
) -> schemas.JobResponse:
    """
    Get job details by ID including the document information
    """
    return utils.get_job(db, job_id)

@router.put("/{job_id}/{action}")
async def update_job_status(
    job_id: int,
    action: str,
    background_task: BackgroundTasks,
    db: Session = Depends(get_db)
) -> schemas.JobResponse:
    """
    Update job status through approve/reject actions.
    Action must be either 'approve' or 'reject'.
    """
    if action not in ["APPROVE", "REJECT"]:
        raise HTTPException(status_code=400, detail="Invalid action")
    return service.update_job_status(db, job_id, action, background_task)
