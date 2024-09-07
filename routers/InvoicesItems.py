# routers/invoice_items.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Flower_Buy.crud import InvoiceItems
from Flower_Buy.schemas.InvoiceItems import InvoiceItemCreate, InvoiceItem
from Flower_Buy.database import get_db
from .. import crud, schemas, database

router = APIRouter()

# Create a new invoice item
@router.post("/invoices_items", response_model=schemas.InvoiceItem)
def create_invoice_item(invoice_item: InvoiceItemCreate, db: Session = Depends(get_db)):
    item = crud.create_invoice_item(db, invoice_item)
    if not item:
        raise HTTPException(status_code=404, detail="Product not found")
    return item
