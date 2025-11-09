from celery import Celery
import os

# Get Redis URL from environment variable or use default
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# Create Celery instance
celery_app = Celery(
    "protocol_library",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=[
        "core.celery.tasks.document_tasks",  # Include your task modules here
    ]
)

# Optional configurations
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes timeout
    worker_prefetch_multiplier=1,  # Disable prefetching for long-running tasks
    task_acks_late=True,  # Tasks are acknowledged after completion
)

# Optional: Add periodic tasks if needed
celery_app.conf.beat_schedule = {
    # Example periodic task
    # 'cleanup-old-files': {
    #     'task': 'core.celery.tasks.document_tasks.cleanup_old_files',
    #     'schedule': 60.0 * 60.0,  # Run every hour
    # },
}
