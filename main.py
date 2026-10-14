from fastapi import FastAPI
from models import Product

type json = str | bytes | bytearray
app = FastAPI()


products: list[Product] = [
    Product(
        name="Beans",
        unit="kg",
        cost_per_unit=12.50,
        price_per_unit=24.99,
        quantity_in_stock=150.0,
    ),
    Product(
        name="Stainless Steel Travel Mug",
        unit="piece",
        cost_per_unit=4.20,
        price_per_unit=15.00,
        quantity_in_stock=85.0,
    ),
    Product(
        name="Oat Milk (Barista Blend)",
        unit="liter",
        cost_per_unit=1.15,
        price_per_unit=3.49,
        quantity_in_stock=320.0,
    ),
    Product(
        name="Vanilla Syrup",
        unit="bottle",
        cost_per_unit=3.80,
        price_per_unit=9.99,
        quantity_in_stock=42.0,
    ),
    Product(
        name="Biodegradable Coffee Filters",
        unit="pack",
        cost_per_unit=0.75,
        price_per_unit=2.99,
        quantity_in_stock=500.0,
    ),
]


@app.get("/")
def print_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def get_name(name: str):
    return {"message": f"hello {name}"}


@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product


@app.get("/products")
def get_products():
    return products


@app.get("/products/search")
def search_product(name: str, unit: str = ""):
    filtered_products = [p for p in products if name.lower() in p.name.lower()]

    if unit:
        filtered_products = [p for p in filtered_products if p.unit == unit]

    return filtered_products
