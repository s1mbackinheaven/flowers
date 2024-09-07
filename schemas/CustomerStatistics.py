from pydantic import BaseModel
from datetime import date

class CustomerStatisticBase(BaseModel):
    date_range: date
    total_purchases: int
    total_amount_spent: int

class CustomerStatisticCreate(CustomerStatisticBase):
    customer_id: int

class CustomerStatistic(CustomerStatisticBase):
    customer_statistic_id: int
    customer_id: int

    class Config:
        orm_mode = True
