from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Flower_Buy.crud import Invoices
from Flower_Buy.schemas.Invoices import InvoiceCreate, Invoice
from .. import crud, schemas, database
from Flower_Buy.database import get_db

router = APIRouter()

@router.post("/invoices/", response_model=schemas.Invoice)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return crud.create_invoice(db, invoice)

@router.get("/invoices/recent/{customer_id}", response_model=schemas.Invoice)
def get_recent_invoice(customer_id: int, db: Session = Depends(get_db)):
    invoice = crud.get_recent_invoice(db, customer_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.get("/invoices/{customer_id}", response_model=schemas.InvoiceListResponse)
def get_invoices_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_invoices_by_customer(db, customer_id)
