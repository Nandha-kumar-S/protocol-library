from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from ml.stages.processors import handle_job_flows
from utils.schema_processor import process_individual_schemas
from sqlalchemy.orm import Session
from db.database import get_db


router = APIRouter(prefix="/api/utility", tags=["Utility APIs"])

class SchemaProcessRequest(BaseModel):
    schemas_dir: str
    document_id: int
    json_type: str
    
@router.post("/process-schemas")
async def process_schemas(request: SchemaProcessRequest, db: Session = Depends(get_db)) -> dict:
    """
    API endpoint to process individual schema files from a directory
    
    Args:
        request (SchemaProcessRequest): Contains the directory path of schema files
        
    Returns:
        dict: Status of the operation
    """
    try:
        process_individual_schemas(db=db,
                                   schemas_dir=request.schemas_dir,
                                   document_id=request.document_id,
                                   json_type=request.json_type
                                   )
        return {
            "status": "success",
            "message": "Successfully processed schema files from directory"
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing schemas: {str(e)}")


@router.get("/run-stages")
async def run_stages(job_id: int) -> dict:
    """
    API endpoint to run all stages for a document
    
    Args:
        db (Session): Database session
    """

    return handle_job_flows(job_id=job_id)
