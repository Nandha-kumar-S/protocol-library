from fastapi import FastAPI
from .router import router

def init_test_users_module(app: FastAPI) -> None:
    """Initialize the test users module"""
    app.include_router(router)
