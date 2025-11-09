from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from db.database import get_db

# Sample Pydantic model for data validation
class ItemCreate(BaseModel):
    name: str
    description: str

# Sample SQLAlchemy model
from sqlalchemy import Column, Integer, String
from db.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Sample CRUD operations with dependency injection
def create_item(db: Session, item: ItemCreate) -> Item:
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session) -> List[Item]:
    return db.query(Item).all()

# Example FastAPI endpoint using dependency injection
from fastapi import APIRouter

router = APIRouter()

@router.post("/items/", response_model=None)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@router.get("/items/", response_model=List[Item])
def list_items(db: Session = Depends(get_db)):
    return get_items(db=db)
