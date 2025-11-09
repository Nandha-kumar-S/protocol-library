import os
import json
from pathlib import Path
from typing import Dict, Any, List
from modules.document.utils import create_document_json
from modules.document import schemas
import json
from pathlib import Path
from typing import Dict, Any, List
from sqlalchemy.orm import Session


def process_individual_schemas(db: Session, schemas_dir: str, document_id: int, json_type: str) -> None:
    """
    Process all JSON files in the individual_schemas directory.
    Each file is processed as an individual schema with the filename as schema_name.
    
    Args:
        schemas_dir (str): Path to the directory containing individual schema JSON files
    """
    schemas_path = Path(schemas_dir)
    
    if not schemas_path.exists() or not schemas_path.is_dir():
        raise ValueError(f"Directory not found: {schemas_dir}")
    
    # Process each JSON file in the directory
    for json_file in schemas_path.glob("*.json"):
        try:
            # Skip system files like .DS_Store
            if json_file.name.startswith('.'):
                continue
                
            # Read the JSON content
            with open(json_file, 'r') as f:
                json_content = json.load(f)
            
            # Get schema name from filename (remove .json extension)
            schema_name = json_file.stem
            print(f"Processing schema: {schema_name}")
            
            # Create document JSON with schema name and INDIVIDUAL_SCHEMA type
            # Create document JSON with schema name and INDIVIDUAL_SCHEMA type
            document_json = schemas.JsonValueCreate(
                document_id=document_id,
                schema_name=schema_name,
                json_type=json_type,
                json_value=json_content,
            )
            response = create_document_json(db=db, document_json=document_json)
            
            print(f"Successfully processed {schema_name=}: {response=}")
            
        except Exception as e:
            print(f"Error processing {json_file.name}: {str(e)}")
            continue
