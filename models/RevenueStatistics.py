from sqlalchemy import Column, Integer, Date, BigInteger

from Flower_Buy.database import Base

class RevenueStatistics(Base):
    __tablename__ = 'revenue_statistics'

    statistics_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_range = Column(Date, nullable=False)
    total_revenue = Column(BigInteger, nullable=False)