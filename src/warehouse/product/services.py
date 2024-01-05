from uuid import uuid4
from sqlalchemy.orm import Session
from src.warehouse.models import Product
from src.warehouse.product.schemas import ProductSchemaRequest
from sqlalchemy.exc import IntegrityError, DataError
from fastapi import HTTPException


class ProductServices:

    @staticmethod
    def list_all_products(db: Session):
        return db.query(Product).all()

    @staticmethod
    def create_product(db: Session, product: ProductSchemaRequest):
        try:
            db_product = Product(product.name)
            db_product.department_id = product.department_id
            db_product.description = product.description
            db_product.code = product.code
            db_product.size = product.size
            db_product.weight = product.weight
            db_product.id = uuid4()

            db.add(db_product)
            db.flush()
            db.refresh(db_product)

            return db_product

        except IntegrityError as ex:
            db.rollback()
            raise HTTPException(status_code=400, detail='Product already exists.')

        except Exception as ex:
            db.rollback()
            raise HTTPException(status_code=500, detail="Internal Error.")

    @staticmethod
    def get_one_product(db:Session, product_id: str):
        try:
            return db.query(Product).get(product_id)

        except DataError as ex:
            raise HTTPException(status_code=404, detail="Product not found.")

        except Exception as ex:
            raise HTTPException(status_code=500, detail='Internal Error')