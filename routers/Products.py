from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models, database

router = APIRouter()

@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return crud.create_product(db, product)

@router.get("/products/{product_id}", response_model=schemas.Product)
def read_products(product_id: int, db: Session = Depends(database.get_db)):
    db_product = crud.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/products/{product_id}", response_model=schemas.Product)
def update_products(product_id: int, product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    update_product = crud.get_product(db, product_id)
    if update_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return update_product

@router.delete("/products/{product_id}", response_model=schemas.Product)
def delete_products(product_id: int, db: Session = Depends(database.get_db)):
    delete_product = crud.get_product(db, product_id)
    if delete_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return delete_product
