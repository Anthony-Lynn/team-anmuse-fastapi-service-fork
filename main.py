from fastapi import FastAPI
from models import Product

app = FastAPI()


products: list[Product] = []


@app.get("/")
def print_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def get_name(name: str):
    return {"message": f"hello {name}"}


@app.post("/products", status_code=201)
def create_product(product: Product):
    products.append(product)
    return product


@app.get("/products")
def get_products():
    return products


@app.get("/products/search")
def search_product(name: str, unit: str = "each"):
    filtered_products = [p for p in products if name.lower() in p.name.lower()]
    filtered_products = [p for p in filtered_products if p.unit == unit]

    return filtered_products
