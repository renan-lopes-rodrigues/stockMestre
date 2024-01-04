import datetime
from pydantic import UUID4, BaseModel
# from src.core.company.schemas import CompanySchemaRequest
from src.schemas import ItemBase


class CountrySchemaDetailed(ItemBase):
    continent: ItemBase

class StateSchemaDetail(ItemBase):
    country: CountrySchemaDetailed


class CompanySchemaBasic(BaseModel):
    id: UUID4
    email: str
    active: bool
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None
