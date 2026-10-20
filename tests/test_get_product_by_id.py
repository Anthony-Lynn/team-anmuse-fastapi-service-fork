from tests.conftest import create_product


def test_get_product_by_id_returns_created_product(client):
    created = create_product(client, name="syrup").json()

    response = client.get(f"/products/{created['id']}")

    assert response.status_code == 200
    product = response.json()
    assert product["id"] == created["id"]
    assert product["name"] == "syrup"
    assert product["unit"] == "bottle"
    assert product["price_per_unit"] == 3.07
    assert product["quantity_in_stock"] == 6
    assert "cost_per_unit" not in product


def test_get_product_by_id_returns_404_when_missing(client):
    response = client.get("/products/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_get_product_by_id_returns_422_for_non_integer_id(client):
    response = client.get("/products/not-an-id")

    assert response.status_code == 422
