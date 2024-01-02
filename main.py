from fastapi import FastAPI
# from src import resources
from src.warehouse import resources
from src.warehouse import models
from src.database.data_base_config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(resources.router)
