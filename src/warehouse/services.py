from sqlalchemy.orm import Session
from src.warehouse.models import Product


class ListProductsServices:
    # def __init__(self):
    #     # self.product_model: Product = Product()


    @staticmethod
    def list_all_products(db: Session):
        return db.query(Product).all()