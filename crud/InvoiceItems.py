# crud/invoice_items.py
from sqlalchemy.orm import Session
from Flower_Buy.models import InvoiceItems, Product
from Flower_Buy.schemas.InvoiceItems import InvoiceItemCreate
from Flower_Buy.crud.Invoices import update_invoice_total_amount

# Create a new invoice item and update invoice total amount
def create_invoice_item(db: Session, invoice_item: InvoiceItemCreate):
    product = db.query(Product).filter(Product.product_id == invoice_item.product_id).first()
    if not product:
        return None

    # Calculate subtotal
    subtotal = product.price * invoice_item.quantity

    new_invoice_item = InvoiceItems(
        invoice_id=invoice_item.invoice_id,
        product_id=invoice_item.product_id,
        quantity=invoice_item.quantity,
        subtotal=subtotal
    )
    db.add(new_invoice_item)
    db.commit()


    update_invoice_total_amount(db, invoice_item.invoice_id)

    db.refresh(new_invoice_item)
    return new_invoice_item
