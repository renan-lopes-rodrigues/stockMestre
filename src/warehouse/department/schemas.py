from pydantic import UUID4
from src.schemas import ItemBaseResponse

class DepartmentListResponse(ItemBaseResponse):
    id: UUID4
