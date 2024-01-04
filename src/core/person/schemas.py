from enum import Enum

from pydantic import UUID4, BaseModel
from src.schemas import ItemBase, ItemBaseResponse
from src.core.schemas import StateSchemaDetail
# from src.core.company.schemas import CompanySchemaDetail


class PersonType(Enum):
    one = "physical"
    two = "legal"

class PersonSchemaRequest(BaseModel):
    name: str
    type: PersonType
    address: str
    number: str
    neighborhood: str
    city: str
    state_id: int
    cep: str
    complement: str | None = None
    document: str

class PersonSchemaDetail(ItemBaseResponse):
    id: UUID4
    name: str
    type: PersonType
    address: str
    number: str
    neighborhood: str
    city: str
    state: StateSchemaDetail
    cep: str
    complement: str | None = None
    document: str
    # companies: list[CompanySchemaDetail]

