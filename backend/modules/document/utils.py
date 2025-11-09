
from fastapi import HTTPException
from modules.document import models, schemas
from db.database import Session


def create_document_json(document_json: schemas.JsonValueCreate, db: Session) -> dict:
    """
    Create JSON value for document
    """
    db_document_json = models.JsonValues(
        document_id=document_json.document_id,
        json_type=document_json.json_type,
        schema_name=document_json.schema_name,
        json_value=document_json.json_value,
    )
    
    db.add(db_document_json)
    db.commit()
    db.refresh(db_document_json)

    return {
        "id": db_document_json.id,
        "document_id": db_document_json.document_id,
        "schema_name": db_document_json.schema_name,
        "json_type": db_document_json.json_type,
    }



def update_document_json(
    db: Session,
    document_id: int,
    json_type: str,
    json_value: dict | list,
    schema_name: str = None,
    use_reviewed_json: bool = True
) -> dict:
    """
    Update/Insert logic for specific JSON type for document.
    
    If 'REVIEWED_<json_type>' entry exists, update the json_value.
    Otherwise, create a new row with json_type='REVIEWED_<json_type>'. -> applicable only if use_reviewed_json is True.
    If use_reviewed_json is False, it will update or create the original json_type entry
    """
    # 1. Check if the document exists
    document = db.query(models.Document).filter(
        models.Document.id == document_id,
        models.Document.is_deleted == False
    ).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    if use_reviewed_json:
        # Construct the reviewed JSON type string only if use_reviewed_json is True.
        # There might be some cases, where you want to just replace the older record (example: during creation of json in ML stages)
        reviewed_json_type = f"REVIEWED_{json_type}"
    else:
        reviewed_json_type = json_type
    
    # 2. Check if a reviewed entry already exists for this document and type
    json_entry = db.query(models.JsonValues).filter(
        models.JsonValues.document_id == document_id,
        models.JsonValues.json_type == reviewed_json_type,
        models.Document.is_deleted == False,
        models.JsonValues.schema_name == schema_name if schema_name else True
    ).first()
    
    if json_entry:
        # 3. If an entry exists, update it
        json_entry.json_value = json_value
        json_entry.schema_name = schema_name
        db.commit()
        db.refresh(json_entry)
        
        return {
            "message": f"Successfully updated reviewed JSON entry for document {document_id}",
            "json_entry_id": json_entry.id
        }
    else:
        # 4. If an entry does not exist, create a new one
        new_json_entry = models.JsonValues(
            document_id=document_id,
            json_type=reviewed_json_type,
            json_value=json_value,
            schema_name=schema_name
        )
        
        db.add(new_json_entry)
        db.commit()
        db.refresh(new_json_entry)
        
        return {
            "message": f"Successfully created new reviewed JSON entry for document {document_id}",
            "json_entry_id": new_json_entry.id
        }


def get_document_json(db: Session, document_id: int, json_type: str, schema_name: str = None) -> dict:
    """
    Get specific JSON type for document
    """
    # First, try to get the reviewed version
    if isinstance(json_type, models.JsonType):
        json_type = json_type.value

    reviewed_json_type = f"REVIEWED_{json_type}"
    json_value = db.query(models.JsonValues).filter(
        models.JsonValues.document_id == document_id,
        models.Document.is_deleted == False,
        models.JsonValues.json_type == reviewed_json_type,
        (models.JsonValues.schema_name == schema_name if schema_name else True)
    ).first()

    # If the reviewed version doesn't exist, fall back to the original
    if not json_value:
        json_value = db.query(models.JsonValues).filter(
            models.JsonValues.document_id == document_id,
            models.Document.is_deleted == False,
            models.JsonValues.json_type == json_type,
            (models.JsonValues.schema_name == schema_name if schema_name else True)
        ).first()
    
    if not json_value:
        return {}
    
    # Convert SQLAlchemy model to Pydantic and then to dict
    return json_value.to_dict()



def get_document(db: Session, document_id: int) -> schemas.DocumentResponse:
    """
    Get document by ID
    """
    document = db.query(models.Document).filter(
        models.Document.id == document_id,
        models.Document.is_deleted == False
    ).first()
    
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return schemas.DocumentResponse.from_orm(document)
