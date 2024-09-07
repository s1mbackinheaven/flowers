from pydantic import BaseModel
from datetime import date

class RevenueStatisticBase(BaseModel):
    date_range: date
    total_revenue: int

class RevenueStatistic(RevenueStatisticBase):
    statistic_id: int

    class Config:
        orm_mode = True
