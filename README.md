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
