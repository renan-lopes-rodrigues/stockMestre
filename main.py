from fastapi import FastAPI
from src import resources 

app = FastAPI()

app.include_router(resources.router)
