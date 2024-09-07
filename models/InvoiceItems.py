from sqlalchemy import Column, Integer, String, Date, BigInteger, ForeignKey
from sqlalchemy.orm import foreign, relationship
# from .Invoices import Invoice
# from .Products import Product

from Flower_Buy.database import Base

class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    item_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoices.invoice_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, index=True)
    subtotal = Column(BigInteger, index=True)

    invoice = relationship('Invoice', back_populates='items')
    product = relationship('Product', back_populates='items')