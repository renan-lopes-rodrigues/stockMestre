from enum import Enum
from pydantic import UUID4, BaseModel
from src.schemas import ItemBase, ItemBaseResponse
from src.core.company.schemas import CompanySchemaDetail
from src.warehouse.product.schemas import ProductSchemaDetail
import datetime

class MeasurementEnum(Enum):
    one = "ML"
    two = "MG"
    three = "UN"

class StokeSchemaRequestIn(ItemBase):
    alias: str
    company_id: UUID4
    product_id: UUID4
    amount: int
    measurement: MeasurementEnum
    price: int
    cost: int
    active: bool

class StokeSchemaRequestOut(BaseModel):
    stoke_id: UUID4
    amount: int

class StokeSchemaDetail(ItemBaseResponse):
    id: UUID4
    alias:str
    company: CompanySchemaDetail
    product: ProductSchemaDetail
    amount: int
    measurement: MeasurementEnum
    price: int
    cost: int
    active: bool
    last_entry: datetime.datetime
    last_sale: datetime.datetime | None = None