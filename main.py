from fastapi import FastAPI
# from src import resources
from src.warehouse import resources
# from src.models import *
from src.database.data_base_config import engine, SessionLocal

# models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

app = FastAPI()

app.include_router(resources.router)
