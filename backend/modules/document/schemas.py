from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from enum import Enum

from modules.document.models import JsonType

    

class JsonValueResponse(BaseModel):
    id: int
    schema_name: Optional[str] = None
    json_value: Optional[Dict | List] = None
    json_type: JsonType
    is_deleted: bool = False

    model_config = {
        "from_attributes": True
    }

class DocumentBase(BaseModel):
    document_url: str

class JsonValueCreate(BaseModel):
    document_id: int
    json_type: JsonType
    schema_name: Optional[str] = None
    json_value: Optional[Dict[str, Any] | List[Dict[str, Any]]] = None


class DocumentCreate(BaseModel):
    
    file: bytes
    filename: str

class DocumentResponse(DocumentBase):
    id: int
    final_json: Optional[Dict[str, Any]] = None
    meta_json: Optional[Dict[str, Any]] = None
    is_deleted: bool = False
    document_url: str
    # json_values: List[JsonValueResponse] = []

    model_config = {
        "from_attributes": True
    }
