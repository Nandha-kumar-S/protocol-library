import os
from pathlib import Path

# Get the base directory (backend folder)
BASE_DIR = Path(__file__).resolve().parent.parent

# Define uploads directory relative to backend folder
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
DOCUMENTS_DIR = os.path.join(UPLOADS_DIR, "documents")

# Create directories if they don't exist
os.makedirs(DOCUMENTS_DIR, exist_ok=True)
