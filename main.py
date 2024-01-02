from fastapi import FastAPI
# from src import resources
from src.warehouse import resources

app = FastAPI()

app.include_router(resources.router)
