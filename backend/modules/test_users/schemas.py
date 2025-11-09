from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str
    is_active: Optional[bool] = True
