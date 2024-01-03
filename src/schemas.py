from pydantic import BaseModel
import datetime

class ItemBase(BaseModel):
    name: str
    description: str | None = None

class ItemBaseResponse(ItemBase):
    created_at: datetime.datetime
    updated_at: datetime.datetime