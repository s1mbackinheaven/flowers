# schemas/invoice_item.py
from pydantic import BaseModel
from typing import Optional

class InvoiceItemBase(BaseModel):
    product_id: int
    quantity: int

class InvoiceItemCreate(InvoiceItemBase):
    invoice_id: int

class InvoiceItem(InvoiceItemBase):
    item_id: int
    subtotal: int

    class Config:
        orm_mode = True
