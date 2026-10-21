from tests.conftest import create_product, product_payload


def create_category(client, name="beverages"):
    return client.post("/categories", json={"name": name})


def test_post_category_creates_category(client):
    response = create_category(client, name="dry goods")

    assert response.status_code == 201
    category = response.json()
    assert category["id"] == 1
    assert category["name"] == "dry goods"


def test_post_category_returns_422_when_name_is_missing(client):
    response = client.post("/categories", json={})

    assert response.status_code == 422


def test_get_category_returns_parent_and_products(client):
    category = create_category(client, name="beverages").json()
    first = create_product(client, name="syrup", category_id=category["id"]).json()
    second = create_product(client, name="oat milk", unit="liter", category_id=category["id"]).json()

    response = client.get(f"/categories/{category['id']}")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == category["id"]
    assert body["name"] == "beverages"
    product_names = {product["name"] for product in body["products"]}
    assert product_names == {first["name"], second["name"]}
    assert len(body["products"]) == 2


def test_get_category_returns_empty_products_when_none_assigned(client):
    category = create_category(client).json()

    response = client.get(f"/categories/{category['id']}")

    assert response.status_code == 200
    assert response.json()["products"] == []


def test_get_category_returns_404_when_missing(client):
    response = client.get("/categories/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"


def test_post_product_associates_category_and_nests_name(client):
    category = create_category(client, name="beverages").json()

    response = client.post(
        "/products",
        json=product_payload(category_id=category["id"]),
    )

    assert response.status_code == 201
    product = response.json()
    assert product["category"] == {"id": category["id"], "name": "beverages"}
    assert "cost_per_unit" not in product

    fetched = client.get(f"/products/{product['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["category"]["name"] == "beverages"


def test_post_product_returns_404_for_unknown_category_id(client):
    response = client.post("/products", json=product_payload(category_id=999))

    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"
    assert client.get("/products").json() == []
