import pytest
from fastapi.testclient import TestClient

from database import Base, engine
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
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as test_client:
        yield test_client
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)  # leave empty tables behind so the app still works


def product_payload(**overrides):
    return {**SAMPLE_PRODUCT, **overrides}


def create_product(client: TestClient, **overrides):
    return client.post("/products", json=product_payload(**overrides))