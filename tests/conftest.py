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


def product_payload(category_id: int, **overrides):
    return {**SAMPLE_PRODUCT, "category_id": category_id, **overrides}


def create_category(client: TestClient, name: str = "test category"):
    return client.post("/categories", json={"name": name})


def create_product(
    client: TestClient, category_id: int | None = None, **overrides
):
    if category_id is None:
        category_response = create_category(client)
        assert category_response.status_code == 201
        category_id = category_response.json()["id"]
    return client.post(
        "/products",
        json=product_payload(category_id=category_id, **overrides),
    )
