from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker, session

# from models import Customer, Invoice, Product, InvoiceItem, CustomerStatistics, RevenueStatistics
from Flower_Buy.models.Customers import Customer
from Flower_Buy.models.Products import Product
# from Flower_Buy.models.Invoices import Invoice
from . import models
# from Flower_Buy.models.Products import Product
# from Flower_Buy.models.InvoiceItems import InvoiceItem
# from Flower_Buy.models.CustomerStatistics import CustomerStatistics
# from Flower_Buy.models.RevenueStatistics import RevenueStatistics

from .database import SessionLocal, engine, Base
from .routers import Customers, Products, Invoices, InvoicesItems

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(Customers.router, prefix="/api", tags=["customers"])
app.include_router(Products.router, prefix="/api", tags=["products"])
app.include_router(Invoices.router, prefix="/api", tags=["invoices"])
app.include_router(InvoicesItems.router, prefix="/api", tags=["invoicesItems"])