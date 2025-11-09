from fastapi import APIRouter, Depends
from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel
from typing import List, Optional

from db.database import Base, get_db_service
from db.db_service import DBService

# Sample SQLAlchemy Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)

# Sample Pydantic Model
class UserCreate(BaseModel):
    email: str
    name: str
    is_active: Optional[bool] = True

router = APIRouter()

@router.post("/users/")
def create_user(user: UserCreate, db: DBService = Depends(get_db_service)):
    # Create a new user instance
    new_user = User(**user.model_dump())
    # Add it to the database - transaction will be committed automatically when the request ends
    return db.add(new_user)

@router.get("/users/")
def get_users(is_active: bool = True, db: DBService = Depends(get_db_service)):
    # Get all active users - no commit needed for read operations
    return db.get(User, is_active=is_active)

@router.get("/users/{email}")
def get_user(email: str, db: DBService = Depends(get_db_service)):
    # Get a single user by email - no commit needed for read operations
    return db.get_one(User, email=email)

@router.put("/users/{email}")
async def update_user(email: str, is_active: bool, db: DBService = Depends(get_db_service)):
    # Example of multiple operations in a single transaction
    user = db.get_one(User, email=email)
    if not user:
        return {"error": "User not found"}
    
    # Update user's active status
    rows_updated = db.update(User, {"is_active": is_active}, email=email)
    # Both operations will be committed automatically when the request ends
    return {"updated": rows_updated}

@router.delete("/users/{email}")
def delete_user(email: str, db: DBService = Depends(get_db_service)):
    # Delete a user - transaction will be committed automatically when the request ends
    return db.delete(User, email=email)

@router.post("/users/bulk")
def bulk_operations(db: DBService = Depends(get_db_service)):
    # Example of multiple operations in a single transaction
    # Create some users
    users = [
        User(email="user1@example.com", name="User 1"),
        User(email="user2@example.com", name="User 2")
    ]
    db.add_all(users)
    
    # Update some existing users
    db.update(User, {"is_active": False}, email="old@example.com")
    
    # Delete some users
    db.delete(User, is_active=False)
    
    # All operations will be committed together when the request ends
    return {"message": "Bulk operations completed"}
