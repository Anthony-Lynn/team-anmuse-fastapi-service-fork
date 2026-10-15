from fastapi import APIRouter

from app.domains.products.product_service import ProductService
from app.domains.products.schemas.product import Product

router = APIRouter()
product_service = ProductService()


@router.post("/products", status_code=201)
def create_product(product: Product):
    return product_service.create_product(product)


@router.get("/products")
def get_products():
    return product_service.get_products()


@router.get("/products/search")
def search_products(name: str, unit: str = "each"):
    return product_service.search_product(name, unit)
