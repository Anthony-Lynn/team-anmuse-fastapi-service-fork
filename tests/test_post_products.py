from tests.conftest import product_payload


def test_post_product_creates_product(client):
    payload = product_payload()

    response = client.post("/products", json=payload)

    assert response.status_code == 201
    product = response.json()
    assert product["id"] == 1
    assert product["name"] == payload["name"]
    assert product["unit"] == payload["unit"]
    assert product["price_per_unit"] == payload["price_per_unit"]
    assert product["quantity_in_stock"] == payload["quantity_in_stock"]
    assert "cost_per_unit" not in product


def test_post_product_allows_zero_cost_and_quantity(client):
    payload = product_payload(cost_per_unit=0, quantity_in_stock=0)

    response = client.post("/products", json=payload)

    assert response.status_code == 201
    assert response.json()["quantity_in_stock"] == 0


def test_post_product_returns_422_when_body_is_missing(client):
    response = client.post("/products")

    assert response.status_code == 422


def test_post_product_returns_422_when_required_field_is_missing(client):
    payload = product_payload()
    payload.pop("name")

    response = client.post("/products", json=payload)

    assert response.status_code == 422


def test_post_product_returns_422_for_invalid_cost_per_unit(client):
    payload = product_payload(cost_per_unit=-1.0)

    response = client.post("/products", json=payload)

    assert response.status_code == 422


def test_post_product_returns_422_for_invalid_quantity_in_stock(client):
    payload = product_payload(quantity_in_stock=-1)

    response = client.post("/products", json=payload)

    assert response.status_code == 422


def test_post_product_returns_422_for_wrong_field_types(client):
    payload = product_payload(price_per_unit="expensive", quantity_in_stock="many")

    response = client.post("/products", json=payload)

    assert response.status_code == 422
