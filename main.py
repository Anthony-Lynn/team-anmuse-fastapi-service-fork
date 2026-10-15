from fastapi import FastAPI

from app.domains.products.product_router import router as product_router

app = FastAPI()
app.include_router(product_router)


@app.get("/")
def print_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def get_name(name: str):
    return {"message": f"hello {name}"}
