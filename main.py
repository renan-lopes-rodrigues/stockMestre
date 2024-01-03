from fastapi import FastAPI
from src.warehouse import resources
from src.warehouse.department.resources import DepartmentResources
from src.core.person.resources import PersonResources
from src.database.data_base_config import engine, SessionLocal

app = FastAPI()

app.include_router(resources.router)
app.include_router(DepartmentResources.router)
app.include_router(PersonResources.router)