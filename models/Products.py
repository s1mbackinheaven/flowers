from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.orm import foreign, relationship
from Flower_Buy.database import Base
# from .InvoiceItems import InvoiceItem

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    price = Column(BigInteger)
    inventory_quantity = Column(Integer)
    category = Column(String(50))

    items = relationship('InvoiceItem', back_populates='product')