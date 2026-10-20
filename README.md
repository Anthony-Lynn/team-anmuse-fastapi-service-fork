For readme:
# team-anmuse-fastapi-service

## About
A lightweight FastAPI service that exposes simple greeting endpoints. Use it as a starting point for building and testing REST APIs with Python, Uvicorn, and Postman. Schemas are dropped and recreated on the app startup during development.

Creates/gets products


## Prerequisites
Clone repository
Install Postman


## Environment Setup
* Step 1: Setup an enviornment by running "python -m venv .venv" in your terminal.
* Step 2: Start the enviornment by running ".venv\Scripts\Activate.ps1" in your terminal.
* Step 3: create .env file with an enviornment variable set to: DATABASE_URL=postgresql+psycopg2://{username}:{password}@{host}:{port}/products_db. This will allow the server to connect psql database.


## Install Steps
pip install -r requirements.txt


## How to Run App
uvicorn main:app --reload
Endpoints:
- Get(http://127.0.0.1:8000)
- Get(http://127.0.0.1:8000/hello/{name})


## How to Test

### Integration tests (pytest + FastAPI TestClient)

These tests live under `tests/` and use FastAPI's `TestClient` against an in-memory SQLite database, so they do not use your PostgreSQL `DATABASE_URL`.

From the project root, with the virtual environment activated and dependencies installed:

```
pytest
```

Run a single endpoint file:

```
pytest tests/test_get_products.py
pytest tests/test_get_product_by_id.py
pytest tests/test_post_products.py
pytest tests/test_put_product.py
pytest tests/test_delete_product.py
```

| File | Endpoint | Scenarios |
| --- | --- | --- |
| `tests/test_get_products.py` | `GET /products` | empty list; returns every created product; response omits `cost_per_unit` |
| `tests/test_get_product_by_id.py` | `GET /products/{product_id}` | found product; 404 when missing; 422 for a non-integer id |
| `tests/test_post_products.py` | `POST /products` | 201 create; zero cost/quantity allowed; 422 missing body, missing field, negative `cost_per_unit`, negative `quantity_in_stock`, wrong types |
| `tests/test_put_product.py` | `PUT /products/{product_id}` | 200 update; 404 when missing; 422 missing field, negative `cost_per_unit`, negative `quantity_in_stock`, non-integer id |
| `tests/test_delete_product.py` | `DELETE /products/{product_id}` | 204 delete and product is gone; 404 when missing; 404 on second delete; 422 for a non-integer id |

### Postman

Create a new postman workspace, then drag the Tests.postman_collection.json file into the "Items in Cloud" section.

Example rroduct endpoint request body:
{
    "name": "syrup",
    "unit": "bottle",
    "cost_per_unit": 4.99,
    "price_per_unit": 3.07,
    "quantity_in_stock": 6
}

Hello Endpoint: http://127.0.0.1:8000/hello
Products Endpoint: http://127.0.0.1:8000/products
Search Produts Endpoint: http://127.0.0.1:8000/products/search
