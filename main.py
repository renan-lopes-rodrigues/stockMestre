from fastapi import FastAPI
from src.warehouse.product.resources import ProductResources
from src.warehouse.department.resources import DepartmentResources
from src.core.person.resources import PersonResources
from src.core.company.resources import CompanyResources
from src.database.data_base_config import engine, SessionLocal

app = FastAPI()

app.include_router(ProductResources.router)
app.include_router(DepartmentResources.router)
app.include_router(PersonResources.router)
app.include_router(CompanyResources.router)