from sqlalchemy.orm import Session
from Flower_Buy.models.Customers import Customer
from Flower_Buy.schemas.Customers import CustomerCreate

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()

# def get_customers(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def update_customer(db: Session, customer_id: int, customer: CustomerCreate):
    db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_customer:
        for key, value in customer.model_dump().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer
