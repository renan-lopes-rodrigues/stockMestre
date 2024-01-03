import datetime
# from uuid import uuid4
from pydantic import BaseModel, UUID4

class ItemBase(BaseModel):
    name: str
    description: str | None = None

class DepartmentList(ItemBase):
    id: UUID4
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

class ProductCreate(ItemBase):
    department_id: int
    code: str
    size: str
    weight: int