from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.warehouse.services import ListProductsServices
from src.database.data_base_config import get_db

router = APIRouter()

@router.get('/stoke/products', tags=["Warehouse Operations"])
def all_products(db: Session = Depends(get_db)):
    return ListProductsServices.list_all_products(db=db)