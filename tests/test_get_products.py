from tests.conftest import create_product


def test_get_products_returns_empty_list(client):
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == []


def test_get_products_returns_all_created_products(client):
    first = create_product(client, name="syrup", unit="bottle")
    second = create_product(client, name="flour", unit="bag")

    response = client.get("/products")

    assert response.status_code == 200
    products = response.json()
    assert len(products) == 2
    names = {product["name"] for product in products}
    assert names == {"syrup", "flour"}
    assert first.json() in products
    assert second.json() in products


def test_get_products_response_omits_cost_per_unit(client):
    create_product(client)

    response = client.get("/products")

    assert response.status_code == 200
    product = response.json()[0]
    assert "cost_per_unit" not in product
    assert product["category"]["name"] == "test category"
    assert set(product.keys()) == {
        "id",
        "name",
        "unit",
        "price_per_unit",
        "quantity_in_stock",
        "category",
    }
