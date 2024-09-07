from sqlalchemy import Column, Integer, String, Date, BigInteger
from Flower_Buy.database import Base
# from .CustomerStatistics import CustomerStatistics
# from .Invoices import Invoice

from sqlalchemy.orm import relationship

class Customer(Base):

    customer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(60))
    date_of_birth = Column(Date)
    email = Column(String(60))
    phone_number = Column(String(11))
    hometown = Column(String(20))
    loyalty_level = Column(String(10))
    total_spent = Column(BigInteger)

    __tablename__ = 'customers'

    class Config:
        orm_mode = True
        migrate = True

    invoices = relationship('Invoice', back_populates='customer')
    # statistics = relationship('CustomerStatistics', back_populates='customer')
