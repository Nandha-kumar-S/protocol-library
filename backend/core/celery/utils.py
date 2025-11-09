from functools import wraps
from celery.result import AsyncResult
from core.celery.celery_app import celery_app

def get_task_status(task_id: str) -> dict:
    """
    Get the status of a Celery task
    
    Args:
        task_id (str): The ID of the task to check
        
    Returns:
        dict: Task status information
    """
    task = AsyncResult(task_id, app=celery_app)
    
    response = {
        "task_id": task.id,
        "status": task.status,
        "result": task.result if task.status == "SUCCESS" else None,
    }
    
    if task.failed():
        response["error"] = str(task.result)
    
    return response

def handle_task_failure(task_func):
    """
    Decorator to handle task failures gracefully
    """
    @wraps(task_func)
    def wrapper(*args, **kwargs):
        try:
            return task_func(*args, **kwargs)
        except Exception as e:
            # Log the error or handle it as needed
            raise
    return wrapper
