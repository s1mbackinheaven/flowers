from sqlalchemy import Column, Integer, Date, BigInteger, ForeignKey
from sqlalchemy.orm import  relationship
from .Customers import Customer

from Flower_Buy.database import Base

class CustomerStatistics(Base):
    __tablename__ = 'customer_statistics'
    customer_statistic_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    date_range = Column(Date, nullable=False)
    total_purchased = Column(Integer, nullable=False)
    total_amount_spent = Column(BigInteger, nullable=False)

    customer = relationship('Customer', back_populates='statistics')