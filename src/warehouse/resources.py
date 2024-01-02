from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.warehouse.department.services import DepartmentServices
from src.warehouse.services import ListProductsServices
from src.database.data_base_config import get_db
from src.warehouse.schemas import DepartmentList, ItemBase

router = APIRouter()

@router.get('/stoke/products', tags=["Warehouse Operations"])
def all_products(db: Session = Depends(get_db)):
    return ListProductsServices.list_all_products(db=db)

@router.post('/stoke/departments', response_model=DepartmentList, tags=["Warehouse Operations"])
def create_department(department: ItemBase, db:Session = Depends(get_db)):
    return DepartmentServices.create_department(db=db, department=department)