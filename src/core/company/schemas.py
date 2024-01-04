from pydantic import UUID4, BaseModel
from src.schemas import ItemBaseResponse
from src.core.person.schemas import PersonSchemaDetail
import datetime
class CompanySchemaRequest(BaseModel):
    person_id: UUID4
    email: str
    active: bool
    name: str

class CompanySchemaDetail(ItemBaseResponse):
    id: UUID4
    person: PersonSchemaDetail
    email: str
    active: bool
    name: str