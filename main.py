from fastapi import FastAPI
from src.warehouse import resources
from src.database.data_base_config import engine, SessionLocal

# def get_db():
#     db = SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()

app = FastAPI()

app.include_router(resources.router)
