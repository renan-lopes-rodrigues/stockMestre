from sqlalchemy.orm import Session
from src.warehouse.models import Department
from src.schemas import ItemBase
from sqlalchemy.exc import DataError, IntegrityError
from fastapi import HTTPException
from uuid import uuid4

class DepartmentServices:
    """
    Handles department services
    """

    @staticmethod
    def create_department(db: Session, department: ItemBase):
        try:
            db_department = Department(name=department.name)
            db_department.id = uuid4()
            db_department.description = department.description
            db.add(db_department)
            db.flush()
            db.refresh(db_department)
            return db_department

        except IntegrityError as ex:
            db.rollback()
            raise HTTPException(status_code=400, detail='Product already exists.')

        except Exception as ex:
            db.rollback()
            raise HTTPException(status_code=500, detail="Internal Error.")

    @staticmethod
    def get_all_departments(db: Session):
        try:
            return db.query(Department).all()
        except Exception as ex:
            raise HTTPException(status_code=500, detail='Internal Error')

    @staticmethod
    def get_one_department_by_id(db:Session, department_id: str):
        try:
            return db.query(Department).get(department_id)

        except DataError as ex:
            raise HTTPException(status_code=404, detail="Department not found.")

        except Exception as ex:
            raise HTTPException(status_code=500, detail='Internal Error')