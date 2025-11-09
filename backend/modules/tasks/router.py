from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from db.database import get_db
from utils.utils import run_in_background

router = APIRouter()

def sample_background_task(data: dict):
    import time
    time.sleep(5)
    print(f"Background task finished with data: {data}")

@router.post("/sample_background")
async def trigger_sample_background(data: dict, background_tasks: BackgroundTasks):
    """Endpoint to trigger a sample background task using the util method."""
    run_in_background(background_tasks, sample_background_task, data)
    return {"message": "Background task started."}

@router.post("/usdm_search")
async def search_usdm(
    query: str,
    filters: Dict[str, Any] = None,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    Search USDM content across processed documents
    """
    # TODO: Implement USDM search functionality
    return {"results": [], "total": 0}

@router.get("/usdm_search/{search_id}")
async def get_search_results(
    search_id: str,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """
    Get results of a previously executed search
    """
    # TODO: Implement search results retrieval
    return {"results": [], "total": 0}
