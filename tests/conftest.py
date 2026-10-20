import pytest
from fastapi.testclient import TestClient

import database
from database import Base

from main import app

SAMPLE_PRODUCT = {
    "name": "syrup",
    "unit": "bottle",
    "cost_per_unit": 4.99,
    "price_per_unit": 3.07,
    "quantity_in_stock": 6,
}

@pytest.fixture
def client():
    Base.metadata.drop_all(bind=database.engine)
    Base.metadata.create_all(bind=database.engine)
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(bind=database.engine)


def product_payload(**overrides):
    return {**SAMPLE_PRODUCT, **overrides}


def create_product(client: TestClient, **overrides):
    return client.post("/products", json=product_payload(**overrides))
