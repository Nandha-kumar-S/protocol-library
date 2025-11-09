from datetime import datetime, timezone, timedelta
from typing import List

from models.job import Job, JobStatus, JobHistory

# A simple in-memory list to act as our database
mock_jobs: List[Job] = [
    Job(
        id=1,
        name="Pfizer- Sunitinib Phase 2_3 trial",
        filename="Pfizer- Sunitinib Phase 2_3 trial.pdf",
        submitted_at=datetime.now(timezone.utc) - timedelta(hours=1),
        status=JobStatus.READY_TO_PROCESS,
        history=[
            JobHistory(action="Job created from Pfizer- Sunitinib Phase 2_3 trial.pdf", user="nandhakumar@saama.com")
        ],
        pdf_section_reference={
            "document_type": "Protocol",
            "version": "1.0",
            "section_1": {
                "title": "Introduction",
                "content_ref": "pages 1-3"
            }
        }
    ),
    Job(
        id=2,
        name="Pfizer- Sunitinib Phase 2_3 trial",
        filename="Pfizer- Sunitinib Phase 2_3 trial.pdf",
        submitted_at=datetime.now(timezone.utc) - timedelta(hours=1),
        status=JobStatus.COMPLETED,
        history=[
            JobHistory(action="Job created from Pfizer- Sunitinib Phase 2_3 trial.pdf", user="nandhakumar@saama.com")
        ],
        pdf_section_reference={
            "document_type": "Protocol",
            "version": "1.0",
            "section_1": {
                "title": "Introduction",
                "content_ref": "pages 1-3"
            }
        }
    )
]
