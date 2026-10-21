import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

os.environ["DATABASE_URL"] = "sqlite://"

import database
from database import Base, get_db

test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

database.engine = test_engine
database.SessionLocal = TestingSessionLocal

from main import app

SAMPLE_PRODUCT = {
    "name": "syrup",
    "unit": "bottle",
    "cost_per_unit": 4.99,
    "price_per_unit": 3.07,
    "quantity_in_stock": 6,
}


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)


def product_payload(**overrides):
    return {**SAMPLE_PRODUCT, **overrides}


def create_product(client: TestClient, **overrides):
    return client.post("/products", json=product_payload(**overrides))