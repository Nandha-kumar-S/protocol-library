import os
from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile
from ml.stages.processors import handle_job_flows
from modules.jobs.service import create_job
from modules.document import models, schemas
from utils.utils import run_in_background
from fastapi import BackgroundTasks


async def create_document(db: Session, file: UploadFile, background_tasks: BackgroundTasks) -> dict:
    """
    Create document and store the PDF file locally
    
    Args:
        db (Session): Database session
        file (UploadFile): The uploaded PDF file
        
    Returns:
        schemas.DocumentResponse: The created document information
        
    Raises:
        HTTPException: If file is not a PDF or if there's an error saving the file
    """
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )
    
    try:
        # Create unique filename using timestamp
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{file.filename}"
        
        # Create full file path
        from core.constants import DOCUMENTS_DIR
        file_path = os.path.join(DOCUMENTS_DIR, filename)
        
        # Save file
        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)
            
        # Create relative URL for storage in database
        document_url = f"uploads/documents/{filename}"
        
        # Create document record
        db_document = models.Document(document_url=document_url)
        db.add(db_document)
        db.commit()
        db.refresh(db_document)

        job_response = create_job(db, db_document.id)

        run_in_background(background_tasks, handle_job_flows, job_response.id)

        created_response = {
            "document": schemas.DocumentResponse.from_orm(db_document),
            "job": job_response
        }
        
        return created_response
        
    except Exception as e:
        # Clean up file if it was created but database operation failed
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(
            status_code=500,
            detail=f"Error creating document: {str(e)}"
        )

