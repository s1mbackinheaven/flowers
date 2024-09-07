from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/customers/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(database.get_db)):
    return crud.create_customer(db, customer)

@router.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(database.get_db)):
    db_customer = crud.get_customer(db, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.put("/customers/{customer_id}", response_model=schemas.Customer)
def update_customer(customer_id: int, customer: schemas.CustomerCreate, db: Session = Depends(database.get_db)):
    updated_customer = crud.update_customer(db, customer_id, customer)
    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/customers/{customer_id}", response_model=schemas.Customer)
def delete_customer(customer_id: int, db: Session = Depends(database.get_db)):
    deleted_customer = crud.delete_customer(db, customer_id)
    if deleted_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return deleted_customer
