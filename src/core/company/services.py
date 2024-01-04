from sqlalchemy.orm import Session
from src.core.company.schemas import CompanySchemaRequest
from src.core.models import Company
from uuid import uuid4
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

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