from fastapi import APIRouter, Depends
from src.database.data_base_config import get_db
from sqlalchemy.orm import Session
from src.warehouse.stoke.schemas import StokeSchemaRequest, StokeSchemaDetail
from src.warehouse.stoke.facade import StokeFacade


class StokeResources:
    """
    Class responsible to Stoke Resources
    """

    router = APIRouter()
    tags = ["Warehouse Operations | Stoke"]

    @router.post('/stoke/new', response_model=StokeSchemaDetail, tags=tags)
    def create_new_stoke(stoke: StokeSchemaRequest,db: Session = Depends(get_db)):
        return StokeFacade.create_new_stoke(db=db, request=stoke)