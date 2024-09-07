from sqlalchemy import Column, Integer, String, Date, BigInteger, ForeignKey, TIMESTAMP, DateTime
from sqlalchemy.orm import foreign, relationship
from datetime import datetime
from Flower_Buy.database import Base
# from .Customers import Customer
# from .InvoiceItems import InvoiceItem


class Invoice(Base):
    __tablename__ = 'invoices'

    invoice_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    date_invoice = Column(Date)
    total_amount = Column(BigInteger)
    status_invoice = Column(String(20))

    class Config:
        orm_mode = True
        migrate = True

    customer = relationship("Customer", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice")