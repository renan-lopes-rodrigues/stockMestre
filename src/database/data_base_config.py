from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATA_BASE_URL = "postgresql://ip172-18-0-36-cldn214snmng00auhmdg-5432.direct.labs.play-with-docker.com"

engine = create_engine(
    SQLALCHEMY_DATA_BASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()