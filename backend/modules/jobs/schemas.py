from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum
from modules.jobs.models import JobStatus

class JobBase(BaseModel):
    document_id: int

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: int
    document_id: int
    current_stage_execution_status: Optional[str] = None
    error_message: Optional[str] = None
    status: JobStatus
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

