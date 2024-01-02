import datetime
# from uuid import uuid4
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None

class DepartmentList(ItemBase):
    id: str
    created_at: str
    updated_at: str

class ProductCreate(ItemBase):
    department_id: int
    code: str
    size: str
    weight: int