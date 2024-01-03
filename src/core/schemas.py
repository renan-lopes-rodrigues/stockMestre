from src.schemas import ItemBase


class CountrySchemaDetailed(ItemBase):
    continent: ItemBase

class StateSchemaDetail(ItemBase):
    country: CountrySchemaDetailed

