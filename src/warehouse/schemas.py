from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None



class ProductCreate(ItemBase):
    department_id: int
    code: str
    size: str
    weight: int