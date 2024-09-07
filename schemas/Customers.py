from pydantic import BaseModel
from datetime import date
from typing import Optional

class CustomerBase(BaseModel):
    full_name: str
    date_of_birth: date
    email: str
    phone_number: str
    hometown: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_id: int
    loyalty_level: Optional[str] = None
    total_spent: Optional[int] = 0

    class Config:
        orm_mode = True
        