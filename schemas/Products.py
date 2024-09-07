from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: int
    inventory_quantity: int
    category: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
