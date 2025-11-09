from core.celery.celery_app import celery_app
from db.database import SessionLocal
import logging

logger = logging.getLogger(__name__)

@celery_app.task(bind=True)
def process_document(self, document_id: int):
    """
    Process an uploaded document in the background
    
    Args:
        document_id (int): ID of the document to process
    """
    try:
        db = SessionLocal()
        # Add your document processing logic here
        # For example:
        # - Extract text
        # - Process schemas
        # - Generate metadata
        logger.info(f"Processing document {document_id}")
        
    except Exception as e:
        logger.error(f"Error processing document {document_id}: {str(e)}")
        raise
    finally:
        db.close()

@celery_app.task(bind=True)
def cleanup_old_files(self):
    """
    Cleanup old temporary files (example periodic task)
    """
    try:
        # Add cleanup logic here
        logger.info("Cleaning up old files")
    except Exception as e:
        logger.error(f"Error during cleanup: {str(e)}")
        raise
