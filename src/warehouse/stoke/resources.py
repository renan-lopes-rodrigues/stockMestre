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

    @router.post('/stoke/in', response_model=StokeSchemaDetail, tags=tags)
    def create_new_stoke(stoke: StokeSchemaRequest,db: Session = Depends(get_db)):
        return StokeFacade.create_new_stoke(db=db, request=stoke)

    @router.get('/stoke/{company_id}', response_model=list[StokeSchemaDetail], tags=tags)
    def get_all_stokes_by_company(company_id: str, db: Session = Depends(get_db)):
        return StokeFacade.get_stoke_by_company_id(db=db, company_id=company_id)