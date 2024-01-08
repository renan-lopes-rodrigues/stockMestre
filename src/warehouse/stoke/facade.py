from src.warehouse.stoke.services import StokeServices
from sqlalchemy.orm import Session
from src.warehouse.stoke.schemas import StokeSchemaRequest
from src.warehouse.models import Stoke
from src.core.company.services import CompanyServices
from src.warehouse.product.services import ProductServices
from datetime import datetime

class StokeFacade:
    """
    Class responsible to organize the services
    """

    @staticmethod
    def create_new_stoke(db: Session, request: StokeSchemaRequest) -> Stoke:
        """
        Creates a new stoke
        """

        ### Verifying if Stoke of this product already exist on this company
        existing_stoke: Stoke = StokeServices.get_stoke_by_product_and_company(
            db = db,
            product_id=request.product_id,
            company_id=request.company_id
        )

        if not existing_stoke:
            ### Verifying if company exists
            CompanyServices.get_one_company_by_id(db=db, company_id=request.company_id)

            ### Verifying if product exists
            ProductServices.get_one_product(db=db, product_id=request.product_id)

            ### Create a new Stoke for product
            response: Stoke = StokeServices.create_new_stoke(db=db, request=request)

        else:
            existing_stoke.amount += request.amount
            existing_stoke.last_entry = datetime.now()
            response = existing_stoke

        db.commit()
        return response