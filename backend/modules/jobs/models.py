from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from db.database import Base
import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from db.database import Base
import enum
from datetime import datetime

class JobStatus(enum.Enum):
    STARTED = "STARTED"
    PARSING = "PARSING"
    PREPROCESSING = "PREPROCESSING"
    MAP_SECTIONS_TO_SCHEMAS = "MAP_SECTIONS_TO_SCHEMAS"
    CONTENT_EXTRACTION = "CONTENT_EXTRACTION"
    CONTENT_EXTRACTION_PAUSED = "CONTENT_EXTRACTION_PAUSED"
    MAP_CONTENT_TO_SCHEMAS = "MAP_CONTENT_TO_SCHEMAS"
    MAP_CONTENT_TO_SCHEMAS_PAUSED = "MAP_CONTENT_TO_SCHEMAS_PAUSED"         # Deprecated
    CONNECT_SCHEMAS = "CONNECT_SCHEMAS"
    LINK_SCHEMAS = "LINK_SCHEMAS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class CurrentStageExecutionStatus(str, enum.Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    status = Column(Enum(JobStatus), default=JobStatus.PARSING)
    current_stage_execution_status = Column(String, nullable=True, default=CurrentStageExecutionStatus.NOT_STARTED)  # e.g., "IN_PROGRESS", "COMPLETED", "FAILED"
    error_message = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship with Document
    document = relationship("Document", back_populates="jobs")
