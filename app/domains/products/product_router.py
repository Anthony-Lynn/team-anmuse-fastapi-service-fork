from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.domains.products.product_service import ProductService
from app.domains.products.schemas.product import ProductCreate, ProductResponse
from database import get_db

router = APIRouter()
product_service = ProductService()


@router.post("/products", status_code=201, response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)


@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return product_service.get_products(db)


@router.get("/products/search", response_model=list[ProductResponse])
def search_products(name: str, unit: str = "each", db: Session = Depends(get_db)):
    return product_service.search_product(db, name, unit)


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = product_service.get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
