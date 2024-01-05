from enum import Enum
from pydantic import UUID4
from src.schemas import ItemBase, ItemBaseResponse


class MeasurementEnum(Enum):
    one = "ML"
    two = "MG"
    three = "UN"

class StokeSchemaRequest(ItemBase):
    alias: str
    company_id: UUID4
    product_id: UUID4
    amount: int
    measurement: MeasurementEnum
    price: int
    cost: int
    active: bool

class StokeSchemaDetail(ItemBaseResponse):
    alias:str