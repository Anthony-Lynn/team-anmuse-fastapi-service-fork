from tests.conftest import create_category, product_payload


def test_post_product_creates_product(client):
    category = create_category(client).json()
    payload = product_payload(category_id=category["id"])

    response = client.post("/products", json=payload)

    assert response.status_code == 201
    product = response.json()
    assert product["id"] == 1
    assert product["name"] == payload["name"]
    assert product["unit"] == payload["unit"]
    assert product["price_per_unit"] == payload["price_per_unit"]
    assert product["quantity_in_stock"] == payload["quantity_in_stock"]
    assert product["category"] == {"id": category["id"], "name": "test category"}
    assert "cost_per_unit" not in product


def test_post_product_allows_zero_cost_and_quantity(client):
    category = create_category(client).json()
    payload = product_payload(
        category_id=category["id"], cost_per_unit=0, quantity_in_stock=0
    )

    response = client.post("/products", json=payload)

    assert response.status_code == 201
    assert response.json()["quantity_in_stock"] == 0


def test_post_product_returns_422_when_body_is_missing(client):
    response = client.post("/products")

    assert response.status_code == 422


def test_post_product_returns_422_when_required_field_is_missing(client):
    category = create_category(client).json()
    payload = product_payload(category_id=category["id"])
    payload.pop("name")

    response = client.post("/products", json=payload)

    assert response.status_code == 422


def test_post_product_returns_422_when_category_id_is_missing(client):
    payload = {
        "name": "syrup",
        "unit": "bottle",
        "cost_per_unit": 4.99,
        "price_per_unit": 3.07,
        "quantity_in_stock": 6,
    }

    response = client.post("/products", json=payload)

    assert response.status_code == 422
    assert client.get("/products").json() == []


def test_post_product_returns_422_for_invalid_cost_per_unit(client):
    category = create_category(client).json()
    payload = product_payload(category_id=category["id"], cost_per_unit=-1.0)

    response = client.post("/products", json=payload)

    assert response.status_code == 422


def test_post_product_returns_422_for_invalid_quantity_in_stock(client):
    category = create_category(client).json()
    payload = product_payload(category_id=category["id"], quantity_in_stock=-1)

    response = client.post("/products", json=payload)

    assert response.status_code == 422


def test_post_product_returns_422_for_wrong_field_types(client):
    category = create_category(client).json()
    payload = product_payload(
        category_id=category["id"],
        price_per_unit="expensive",
        quantity_in_stock="many",
    )

    response = client.post("/products", json=payload)

    assert response.status_code == 422
