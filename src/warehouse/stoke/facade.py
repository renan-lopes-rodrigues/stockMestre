from src.warehouse.stoke.services import StokeServices
from sqlalchemy.orm import Session
from src.warehouse.stoke.schemas import StokeSchemaRequestIn, StokeSchemaRequestOut
from src.warehouse.models import Stoke
from src.core.company.services import CompanyServices
from src.warehouse.product.services import ProductServices
from datetime import datetime
from fastapi import HTTPException

class StokeFacade:
    """
    Class responsible to organize the services
    """

    @staticmethod
    def create_new_entry_on_stoke(db: Session, request: StokeSchemaRequestIn) -> Stoke:
        """
        Creates a new stoke
        """
        try:
            ### Verifying if Stoke of this product already exist on this company
            existing_stoke: Stoke = StokeServices.get_stoke_by_product_and_company(
                db = db,
                product_id=request.product_id,
                company_id=request.company_id
            )

            ### Verifying if company exists
            existing_company = CompanyServices.get_one_company_by_id(db=db, company_id=request.company_id)
            if not existing_company:
                raise HTTPException(status_code=404, detail='Company not founded.')


            ### Verifying if product exists
            existing_product = ProductServices.get_one_product(db=db, product_id=request.product_id)
            if not existing_product:
                raise HTTPException(status_code=404, detail='Product not founded.')


            elif not existing_stoke:
                # CompanyServices.get_one_company_by_id(db=db, company_id=request.company_id)

                # ProductServices.get_one_product(db=db, product_id=request.product_id)

                ### Create a new Stoke for product
                response: Stoke = StokeServices.create_new_stoke(db=db, request=request)

            else:
                ### Verifying if company exists
                CompanyServices.get_one_company_by_id(db=db, company_id=request.company_id)

                ### Verifying if product exists
                ProductServices.get_one_product(db=db, product_id=request.product_id)

                existing_stoke.amount += request.amount
                existing_stoke.last_entry = datetime.now()
                response = existing_stoke

            db.commit()
            return response

        except Exception as ex:
            raise HTTPException(status_code=500, detail="Internal Error.")

    @staticmethod
    def get_stoke_by_company_id(db: Session, company_id: str) -> list[Stoke]:
        """
        Gets all stokes from company
        """
        try:
            ### Verifying if company exists
            existing_company = CompanyServices.get_one_company_by_id(db=db, company_id=company_id)
            if not existing_company:
                raise HTTPException(status_code=404, detail='Company not founded.')

            response: list(Stoke) = StokeServices.get_stoke_by_company_id(db=db, company_id=company_id)
            return response

        except Exception as ex:
                raise HTTPException(status_code=500, detail="Internal Error.")

    @staticmethod
    def create_new_out_on_stoke(db: Session, request: StokeSchemaRequestOut) -> Stoke:
        """
        Creates a new out on Stoke
        """

        try:
            ### Verify if stoke exists
            stoke: Stoke = db.query(Stoke).get(request.stoke_id)
            if not stoke:
                raise HTTPException(status_code=404, detail="Stoke not Found.")

            if stoke.amount < request.amount:
                raise HTTPException(
                    status_code=400,
                    detail=f"Stoke lower than amount requested to out. Stoke: {stoke.amount}, Amount requested: {request.amount}"
                )

            stoke.amount -= request.amount
            stoke.last_sale = datetime.now()

            db.commit()

            return stoke

        except Exception as ex:
            raise HTTPException(status_code=500, detail="Internal Error.")