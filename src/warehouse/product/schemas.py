from pydantic import UUID4, BaseModel
from src.schemas import ItemBaseResponse, ItemBase
from src.warehouse.department.schemas import DepartmentListResponse

class ProductSchemaDetail(ItemBaseResponse):
    department: DepartmentListResponse
    code: str
    size: str
    weight: int

class ProductSchemaRequest(ItemBase):
    department_id: UUID4
    code: str
    size: str
    weight: int | None = None