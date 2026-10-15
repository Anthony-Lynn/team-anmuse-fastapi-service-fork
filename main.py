from fastapi import FastAPI
from database import Base, engine
from app.domains.products.product_router import router as product_router
from app.domains.products.models.product_model import Product as ProductModel 

app = FastAPI()
app.include_router(product_router)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@app.get("/")
def print_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def get_name(name: str):
    return {"message": f"hello {name}"}
