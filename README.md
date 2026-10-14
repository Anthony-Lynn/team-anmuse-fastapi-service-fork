For readme:
# team-anmuse-fastapi-service

## About
A lightweight FastAPI service that exposes simple greeting endpoints. Use it as a starting point for building and testing REST APIs with Python, Uvicorn, and Postman.

Creates/gets products


## Prerequisites
Clone repository
Install Postman


## Environment Setup
Step 1: Setup an enviornment by running "python -m venv .venv" in your terminal.
Step 2: Start the enviornment by running ".venv\Scripts\Activate.ps1" in your terminal.


## Install Steps
pip install -r requirements.txt


## How to Run App
uvicorn main:app --reload
Endpoints:
- Get(http://127.0.0.1:8000)
- Get(http://127.0.0.1:8000/hello/{name})


## How to Test

Example Data:
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
