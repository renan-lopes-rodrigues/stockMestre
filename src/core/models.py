from src.database.data_base_config import Base
from sqlalchemy import Column, UUID, Integer, String, ForeignKey, DateTime, Boolean, Enum, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

class PersonTypeEnum(enum.Enum):
    one = "physical"
    two = "legal"

class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=True, onupdate=func.now())

    def __init__(self, name):
        self.name = name

class Continent(Base):
    __tablename__ = "continent"
    __table_args__ = (UniqueConstraint('name', name='continent_unique'),)

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = Column(String, nullable=False, unique=True)

    countries = relationship("Country", back_populates="continent")

class Country(Base):
    __tablename__ = "country"
    __table_args__ = (UniqueConstraint('name', name='country_unique'),)

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = Column(String, nullable=False, unique=True)
    continent_id = Column(Integer, ForeignKey("continent.id"), nullable=False)

    continent = relationship(Continent, back_populates="countries")
    states = relationship("State", back_populates="country" )

class State(Base):
    __tablename__ = "state"
    __table_args__ = (UniqueConstraint('name', 'country_id', name='country_state'),)

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)

    persons = relationship("Person", back_populates="state")
    country = relationship(Country, back_populates="states")


class Person(BaseModel):
    __tablename__ = "person"
    __table_args__ = (UniqueConstraint('document', name='person_unique'),)

    type = Column(String, Enum(PersonTypeEnum))
    address = Column(String, nullable=False)
    number = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
    cep = Column(String, nullable=False)
    complement = Column(String, nullable=True)
    document = Column(String, nullable=False, unique=True)

    state = relationship(State, back_populates="persons")
    companies = relationship("Company", back_populates="person")


class Company(BaseModel):
    __tablename__ = "company"

    # id = Column(UUID, primary_key=True, index=True)
    person_id = Column(UUID, ForeignKey("person.id"), nullable=False)
    email = Column(String, nullable=False, unique=True)
    active = Column(Boolean, nullable=False, default=True)

    person = relationship(Person, back_populates="companies")
    stokes = relationship("Stoke", back_populates="company")
