from uuid import uuid4
from sqlalchemy.orm import Session
from src.warehouse.models import Stoke
from sqlalchemy import and_
from src.warehouse.stoke.schemas import StokeSchemaRequestIn
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

class StokeServices:
    """
    Class responsible to StokeServices
    """


    @staticmethod
    def get_stoke_by_product_and_company(db: Session, product_id: str, company_id: str) -> Stoke:
        """
        Gets a Stoke based on product and company
        """

        response: Stoke = db.query(Stoke).filter(and_(Stoke.product_id == product_id, Stoke.company_id==company_id)).first()

        return response


    @staticmethod
    def create_new_stoke(db: Session, request: StokeSchemaRequestIn) -> Stoke:
        """
        Creates a new Stoke for the product
        """
        try:

            new_stoke: Stoke = Stoke(request.name)
            new_stoke.alias = request.alias
            new_stoke.company_id = request.company_id
            new_stoke.product_id = request.product_id
            new_stoke.amount = request.amount
            new_stoke.measurement = request.measurement.value
            new_stoke.price = request.price
            new_stoke.cost = request.cost
            new_stoke.last_entry = datetime.now()
            new_stoke.active = request.active
            new_stoke.id = uuid4()

            db.add(new_stoke)
            db.flush()
            db.refresh(new_stoke)

            return new_stoke

        except IntegrityError as ex:
                db.rollback()
                raise HTTPException(status_code=400, detail='Stoke already exists.')

        except Exception as ex:
            db.rollback()
            raise HTTPException(status_code=500, detail="Internal Error.")

    @staticmethod
    def get_stoke_by_company_id(db: Session, company_id: str) -> list[Stoke]:
        """
        Gets all Stokes by a company
        """

        response: list[Stoke] = db.query(Stoke).filter(Stoke.company_id == company_id).all()
        return response