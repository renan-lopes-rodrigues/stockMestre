from sqlalchemy.orm import Session
from src.warehouse.models import Department
from src.warehouse.schemas import ItemBase
from uuid import uuid4

class DepartmentServices:

    @staticmethod
    def create_department(db: Session, department: ItemBase):
        db_department = Department(name=department.name)
        db_department.id = uuid4()
        db_department.description = department.description
        db.add(db_department)
        db.commit()
        db.refresh(db_department)
        return db_department

    @staticmethod
    def get_all_departments(db: Session):
        return db.query(Department).all()