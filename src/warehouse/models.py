from src.database.data_base_config import Base
from sqlalchemy import Column, UUID, Integer, String, ForeignKey, DateTime, Boolean, CheckConstraint, Enum, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.core.models import BaseModel, Company
import enum

class MeasurementEnum(enum.Enum):
    one = "ML"
    two = "MG"
    three = "UN"

class Department(BaseModel):
    __tablename__ = "department"
    __table_args__ = (UniqueConstraint('name', name='department_unique'),)

    description = Column(String, nullable=False)

    products = relationship("Product", back_populates="department")


class Product(BaseModel):
    __tablename__ = "product"
    __table_args__ = (UniqueConstraint('name', 'department_id', name='prod_department_unique'),)

    department_id = Column(UUID, ForeignKey("department.id"), nullable=False)
    description = Column(String, nullable=False)
    code = Column(String, nullable=True)
    size = Column(String, nullable=False)
    weight = Column(Integer, nullable=True)

    department = relationship(Department, back_populates="products")
    stoke = relationship("Stoke", back_populates='product')

class Stoke(BaseModel):
    __tablename__ = "stoke"
    __table_args__ = (UniqueConstraint('company_id', 'product_id', name='company_prod_unique'),)

    alias = Column(String, nullable=False)
    company_id = Column(UUID, ForeignKey("company.id"), nullable=False)
    product_id = Column(UUID, ForeignKey("product.id"), nullable=False)
    amount = Column(Integer, CheckConstraint('amount >= 0'), nullable=False)
    measurement = Column(String, Enum(MeasurementEnum), nullable=False)
    price = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=True)
    last_sale = Column(DateTime, nullable=True)
    last_entry = Column(DateTime, nullable=True)
    active = Column(Boolean, nullable=False, default=True)

    company = relationship(Company, back_populates='stokes')
    product = relationship(Product, back_populates='stoke')