# team-anmuse-fastapi-service

## About
A lightweight FastAPI service that exposes simple greeting endpoints. Use it as a starting point for building and testing REST APIs with Python, Uvicorn, and Postman. Schemas are dropped and recreated on the app startup during development.

Creates/gets products


## Prerequisites
Clone repository
Install Postman


## Environment Setup
* Step 1: Setup an enviornment by running "python -m venv .venv" in your terminal.
* Step 2: Start the enviornment by running "source .venv\Scripts\Activate.ps1" in your terminal.
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

These tests live under `tests/` and use FastAPI's `TestClient` while connecting directly to the PostgreSQL database configured by `DATABASE_URL` in `.env`. Uvicorn does not need to be running. **Use a dedicated test database:** the fixture drops and recreates the application's tables before each test.

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
| `tests/test_categories.py` | `POST /categories`, `GET /categories/{category_id}` | create category; return category with products; 404 when missing |
| `tests/test_get_products.py` | `GET /products` | empty list; returns every created product; response omits `cost_per_unit` |
| `tests/test_get_product_by_id.py` | `GET /products/{product_id}` | found product; 404 when missing; 422 for a non-integer id |
| `tests/test_post_products.py` | `POST /products` | create product with an existing category; zero cost/quantity allowed; 422 missing body, required field or category, negative values, wrong types; 404 unknown category |
| `tests/test_put_product.py` | `PUT /products/{product_id}` | 200 update including category reassignment; 404 when product/category is missing; 422 missing field/category, invalid values or non-integer id |
| `tests/test_delete_product.py` | `DELETE /products/{product_id}` | 204 delete and product is gone; 404 when missing; 404 on second delete; 422 for a non-integer id |

### Postman

Create a new Postman workspace, then import `Product_API_Tests.postman_collection.json`. Run the requests in order against an empty, dedicated test database; the collection creates a category before sending product requests.

Create a category first with `POST /categories` and use its returned `id` as `category_id` when creating or updating a product.

Example product endpoint request body:
{
    "name": "syrup",
    "unit": "bottle",
    "cost_per_unit": 4.99,
    "price_per_unit": 3.07,
    "quantity_in_stock": 6,
    "category_id": 1
}

Hello Endpoint: http://127.0.0.1:8000/hello
Products Endpoint: http://127.0.0.1:8000/products
Search Produts Endpoint: http://127.0.0.1:8000/products/search
