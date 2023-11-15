from src.database.data_base_config import Base
from sqlalchemy import Column, UUID, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class PersonType(Base):
    __tablename__ = "person_type"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)

    persons = relationship("Person", back_populates="type")

class Continent(Base):
    ___tablename__ = "continent"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = Column(String, nullable=False, unique=True)

    countries = relationship("Contry", back_populates="continent_id")

class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = Column(String, nullable=False, unique=True)
    continent_id = Column(Integer, ForeignKey("continent.id"), nullable=False)

    continent = relationship("Continent", back_populates="countries")
    states = relationship("State", back_populates="country_id" )

class State(Base):
    __tablename__ = "state"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)

    persons = relationship("Person", back_populates="state_id")
    contry = relationship("Country", back_populates="states")


class Person(Base):
    __tablename__ = "person"

    id = Column(UUID, primary_key=True, index=True)
    type = Column(Integer, ForeignKey("person_type.id"))
    address = Column(String, nullable=False)
    number = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state_id = Column(String, ForeignKey("state.id"), nullable=False)
    cep = Column(String, nullable=False)
    complement = Column(String, nullable=True)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False, unique=True)

    state = relationship("State", back_populates="persons")