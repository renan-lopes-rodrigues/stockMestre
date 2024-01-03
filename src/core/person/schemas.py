from enum import Enum

from pydantic import BaseModel
from src.schemas import ItemBase, ItemBaseResponse
from src.core.schemas import StateSchemaDetail


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

class PersonSchemaDetail(BaseModel):
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

