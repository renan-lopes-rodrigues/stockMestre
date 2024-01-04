from sqlalchemy.orm import Session
from src.core.company.schemas import CompanySchemaRequest
from src.core.models import Company
from uuid import uuid4
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, DataError

class CompanyServices:
    """
    Handles Company Services
    """

    @staticmethod
    def create_company(db:Session, company: CompanySchemaRequest):
        try:
            db_company = Company(company.name)
            db_company.person_id = company.person_id
            db_company.email = company.email
            db_company.active = company.active
            db_company.id = uuid4()

            db.add(db_company)
            db.flush()
            db.refresh(db_company)
            return db_company

        except IntegrityError as ex:
            db.rollback()
            raise HTTPException(status_code=400, detail='Company already exists.')

        except Exception as ex:
            db.rollback()
            raise HTTPException(status_code=500, detail='Internal Error.')

    @staticmethod
    def get_all_companies(db: Session):
        return db.query(Company).all()

    @staticmethod
    def get_one_company_by_id(db: Session, company_id: str):
        try:
            return db.query(Company).get(company_id)
        except DataError as ex:
            raise HTTPException(status_code=404, detail="Company not found.")

        except Exception as ex:
            raise HTTPException(status_code=500, detail='Internal Error')