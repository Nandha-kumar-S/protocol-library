from datetime import datetime, timezone, timedelta
from typing import List

from models.job import Job, JobStatus, JobHistory

# A simple in-memory list to act as our database.
#
# The fixtures below are deliberately generic: a sample Phase 2/3 protocol and
# a placeholder user. Real sponsor names and real accounts don't belong in
# seed data that ships with the repo.
mock_jobs: List[Job] = [
    Job(
        id=1,
        name="Sample Phase 2_3 trial protocol",
        filename="sample_phase_2_3_protocol.pdf",
        submitted_at=datetime.now(timezone.utc) - timedelta(hours=1),
        status=JobStatus.READY_TO_PROCESS,
        history=[
            JobHistory(action="Job created from sample_phase_2_3_protocol.pdf", user="demo@example.com")
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
        name="Sample Phase 2_3 trial protocol",
        filename="sample_phase_2_3_protocol.pdf",
        submitted_at=datetime.now(timezone.utc) - timedelta(hours=1),
        status=JobStatus.COMPLETED,
        history=[
            JobHistory(action="Job created from sample_phase_2_3_protocol.pdf", user="demo@example.com")
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
