from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.warehouse.department.services import DepartmentServices
from src.database.data_base_config import get_db
from src.warehouse.schemas import DepartmentList, ItemBase



class DepartmentResources:
    tags = ["Warehouse Operations | Departments"]
    router = APIRouter()

    @router.post('/stoke/departments', response_model=DepartmentList, tags=tags)
    def create_department(department: ItemBase, db:Session = Depends(get_db)):
        return DepartmentServices.create_department(db=db, department=department)

    @router.get('/stoke/departments', response_model=list[DepartmentList], tags=tags)
    def get_all_departments(db:Session = Depends(get_db)):
        return DepartmentServices.get_all_departments(db=db)