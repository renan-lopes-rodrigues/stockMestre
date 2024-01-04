from fastapi import APIRouter, Depends
from src.core.company.schemas import CompanySchemaDetail, CompanySchemaRequest
from sqlalchemy.orm import Session
from src.database.data_base_config import get_db
from src.core.company.services import CompanyServices

class CompanyResources:
    """
    Responsible to Company Resources
    """

    router = APIRouter()
    tags = ["Core | Companies"]

    @router.post('/core/companies',response_model=CompanySchemaDetail, tags=tags)
    def create_company(company: CompanySchemaRequest, db: Session = Depends(get_db)):
        response = CompanyServices.create_company(db=db, company=company)
        db.commit()
        return response

    @router.get('/core/companies', response_model=list[CompanySchemaDetail], tags=tags)
    def get_all_companies(db: Session = Depends(get_db)):
        return CompanyServices.get_all_companies(db=db)

    @router.get('/core/companies/{company_id}', response_model=CompanySchemaDetail, tags=tags)
    def get_one_company(company_id: str, db: Session = Depends(get_db)):
        return CompanyServices.get_one_company_by_id(db=db, company_id=company_id)