from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.warehouse.department.services import DepartmentServices
from src.database.data_base_config import get_db
from src.warehouse.department.schemas import DepartmentListResponse
from src.schemas import ItemBase



class DepartmentResources:
    """
    Responsible to Department Resources
    """
    tags = ["Warehouse Operations | Departments"]
    router = APIRouter()

    @router.post('/stoke/departments', response_model=DepartmentListResponse, tags=tags)
    def create_department(department: ItemBase, db:Session = Depends(get_db)):
        response = DepartmentServices.create_department(db=db, department=department)
        db.commit()
        return response

    @router.get('/stoke/departments', response_model=list[DepartmentListResponse], tags=tags)
    def get_all_departments(db:Session = Depends(get_db)):
        return DepartmentServices.get_all_departments(db=db)

    @router.get('/stoke/departments/{department_id}', response_model=DepartmentListResponse, tags=tags)
    def get_one_department(department_id: str, db:Session = Depends(get_db)):
        return DepartmentServices.get_one_department_by_id(db=db, department_id=department_id)