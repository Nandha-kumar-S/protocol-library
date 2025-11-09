import os
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from utils.job_utils import get_all_jsons_for_json_type
from utils.utils import export_to_excel_sheets, run_in_background
from modules.document import service
from modules.document import utils
from modules.document import schemas
from db.database import get_db
from fastapi import Request
from fastapi import Body, Query
from fastapi import BackgroundTasks


router = APIRouter()

@router.post("/")
async def upload_document(
    background_task: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
) -> dict:
    """Upload a new document and create associated job"""
    return await service.create_document(db, file, background_task)

@router.get("/{document_id}")
async def get_document(
    document_id: int,
    db: Session = Depends(get_db)
) -> schemas.DocumentResponse:
    """Get document details including all JSON states"""
    return utils.get_document(db, document_id)

@router.get("/{document_id}/{json_type}")
async def get_document_json(
    document_id: int,
    json_type: str,
    schema_name: Optional[str] = None,
    db: Session = Depends(get_db),
) -> dict:
    """Get specific JSON type for document"""
    data = utils.get_document_json(db, document_id, json_type, schema_name=schema_name)
    if not data:
        raise HTTPException(status_code=404, detail="JSON data not found")
    return data

@router.put("/{document_id}/{json_type}")
async def update_document_json(
    document_id: int,
    json_type: str,
    schema_name: Optional[str] = Query(None),
    json_value: dict|list = Body(..., embed=True)
    ,
    db: Session = Depends(get_db)
) -> dict:
    """Update specific JSON type for document"""
    return utils.update_document_json(db, document_id, json_type, json_value, schema_name)


@router.get("/export/{document_id}/{json_type}")
async def export_document_json(
    document_id: int,
    json_type: str,
    background_tasks: BackgroundTasks,
    schema_name: Optional[str] = Query(None),
    db: Session = Depends(get_db)
) -> dict:
    """Export specific JSON type for document to Excel"""
    data = get_all_jsons_for_json_type(document_id, json_type)
    if not data:
        raise HTTPException(status_code=404, detail="JSON data not found")
    
    output_filename = f"document_{document_id}_{json_type}.xlsx"
    export_to_excel_sheets(data, output_filename)
    
    # Cleanup: The file will be automatically deleted after response is sent
    run_in_background(background_tasks, os.remove, output_filename)
    
    return FileResponse(
        path=output_filename,
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename=output_filename
    )
