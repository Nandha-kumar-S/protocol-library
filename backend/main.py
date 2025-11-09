from fastapi import FastAPI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware

from modules.jobs.router import router as jobs_router
# from modules.tasks.router import router as tasks_router
from modules.document.router import router as document_router
from modules.utility_apis.routes import router as utility_router
from modules.test_users import init_test_users_module
from core.config.settings import settings
from db.database import init_db

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API to manage PDF processing jobs based on the provided designs."
)

# Initialize database
init_db()

# CORS configuration
origins = settings.BACKEND_CORS_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(jobs_router, prefix="/api/v1/jobs", tags=["jobs"])
app.include_router(document_router, prefix="/api/v1/documents", tags=["documents"])
# app.include_router(tasks_router, prefix="/api/v1/tasks", tags=["tasks"])
app.include_router(utility_router)

# Include test module
if settings.ENVIRONMENT != "production":
    init_test_users_module(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
