from fastapi import APIRouter, Depends
from typing import List
from db.database import get_db_service
from db.db_service import DBService
from .models import User
from .schemas import UserCreate

router = APIRouter(prefix="/test/users", tags=["test-users"])

@router.post("/", response_model=dict)
def create_user(user: UserCreate, db: DBService = Depends(get_db_service)):
    new_user = User(**user.model_dump())
    created_user = db.add(new_user)
    return created_user.to_dict()

@router.get("/", response_model=List[dict])
def get_users(is_active: bool = True, db: DBService = Depends(get_db_service)):
    users = db.get(User, is_active=is_active)
    return [user.to_dict() for user in users]

@router.get("/{email}", response_model=dict)
def get_user(email: str, db: DBService = Depends(get_db_service)):
    user = db.get_one(User, email=email)
    return user.to_dict() if user else {"error": "User not found"}

@router.put("/{email}")
async def update_user(email: str, is_active: bool, db: DBService = Depends(get_db_service)):
    user = db.get_one(User, email=email)
    if not user:
        return {"error": "User not found"}
    
    db.update(User, {"is_active": is_active}, email=email)
    updated_user = db.get_one(User, email=email)
    return updated_user.to_dict()

@router.delete("/{email}")
def delete_user(email: str, db: DBService = Depends(get_db_service)):
    user = db.get_one(User, email=email)
    if not user:
        return {"error": "User not found"}
    
    deleted_count = db.delete(User, email=email)
    return {"message": "User deleted successfully", "deleted": deleted_count}

@router.post("/bulk")
def bulk_operations(db: DBService = Depends(get_db_service)):
    users = [
        User(email="user1@example.com", name="User 1"),
        User(email="user2@example.com", name="User 2")
    ]
    created_users = db.add_all(users)
    
    db.update(User, {"is_active": False}, email="old@example.com")
    db.delete(User, is_active=False)
    
    return {
        "message": "Bulk operations completed",
        "created_users": [user.to_dict() for user in created_users]
    }
    
    return {"message": "Bulk operations completed"}
