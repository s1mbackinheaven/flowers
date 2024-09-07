from pydantic import BaseModel
from datetime import date
from typing import Optional
from datetime import datetime
from typing import List

# from sqlalchemy import TIMESTAMP

class InvoiceBase(BaseModel):
    customer_id: int

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    invoice_id: int
    date_invoice: Optional[date] = None
    total_amount: Optional[int] = 0
    status_invoice: Optional[str] = "Pending"

    class Config:
        orm_mode = True

class InvoiceListResponse(BaseModel):
    invoices: List[Invoice]


