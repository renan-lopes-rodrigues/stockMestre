from src.schemas import ItemBase, ItemBaseResponse
from src.core.schemas import StateSchemaDetail

class PersonSchemaRequest(ItemBase):
    type: str
    address: str
    number: str
    neighborhood: str
    city: str
    state_id: int
    cep: str
    complement: str
    document: str

class PersonSchemaDetail(ItemBaseResponse):
    type: str
    address: str
    number: str
    neighborhood: str
    city: str
    state: StateSchemaDetail
    cep: str
    complement: str
    document: str

