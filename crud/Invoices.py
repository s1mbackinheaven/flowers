from sqlalchemy.orm import Session

from Flower_Buy.models import Customer
from Flower_Buy.models.Invoices import Invoice
from Flower_Buy.schemas.Invoices import InvoiceCreate
from Flower_Buy.models.InvoiceItems import InvoiceItem
from datetime import datetime

def create_invoice(db: Session, invoice: InvoiceCreate):
    db_invoice = Invoice(**invoice.model_dump())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_recent_invoice(db: Session, customer_id: int):
    return db.query(Invoice).filter(Invoice.customer_id == customer_id).order_by(Invoice.date_invoice.desc()).first()

def get_invoices_by_customer(db: Session, customer_id: int):
    return db.query(Invoice).filter(Invoice.customer_id == customer_id).all()

def update_invoice_total_amount(db: Session, invoice_id: int):
    invoice = db.query(Invoice).filter(Invoice.invoice_id == invoice_id).first()
    if not invoice:
        return None
    total_amount = db.query(InvoiceItem).filter(InvoiceItem.invoice_id == invoice_id).with_entities(
        db.func.sum(InvoiceItem.subtotal)
    ).scalar() or 0
    invoice.total_amount = total_amount
    db.commit()
    db.refresh(invoice)
    return invoice