from fastapi import APIRouter
# from src.warehouse.services import ListProductsServices

router = APIRouter()

@router.get('/stoke/products', tags=["Warehouse Operations"])
def all_products():
    # print(ListProductsServices().list_all_products())
    return {"message": None}