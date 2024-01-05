from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.warehouse.product.services import ProductServices
from src.warehouse.product.schemas import ProductSchemaDetail, ProductSchemaRequest
from src.database.data_base_config import get_db


class ProductResources:

    router = APIRouter()
    tags = ["Warehouse Operations | Products"]

    @router.get('/stoke/products', response_model=list[ProductSchemaDetail], tags=tags)
    def all_products(db: Session = Depends(get_db)):
        return ProductServices.list_all_products(db=db)

    @router.post('/stoke/products', response_model=ProductSchemaDetail, tags=tags)
    def create_product(product: ProductSchemaRequest, db: Session = Depends(get_db)):
        response = ProductServices.create_product(db=db, product=product)
        db.commit()
        return response

    @router.get('/stoke/products/{product_id}', response_model=ProductSchemaRequest, tags=tags)
    def get_one_product(product_id: str, db: Session = Depends(get_db)):
        return ProductServices.get_one_product(db=db, product_id=product_id)