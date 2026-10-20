from tests.conftest import create_product, product_payload


def test_put_product_updates_existing_product(client):
    created = create_product(client, name="syrup").json()
    update = product_payload(
        name="flour",
        unit="bag",
        cost_per_unit=2.5,
        price_per_unit=5.0,
        quantity_in_stock=12,
    )

    response = client.put(f"/products/{created['id']}", json=update)

    assert response.status_code == 200
    product = response.json()
    assert product["id"] == created["id"]
    assert product["name"] == "flour"
    assert product["unit"] == "bag"
    assert product["price_per_unit"] == 5.0
    assert product["quantity_in_stock"] == 12
    assert "cost_per_unit" not in product
    assert client.get(f"/products/{created['id']}").json()["name"] == "flour"


def test_put_product_returns_404_when_missing(client):
    response = client.put("/products/999", json=product_payload())

    assert response.status_code == 404
    assert response.json()["detail"] == "No product found"


def test_put_product_returns_422_when_required_field_is_missing(client):
    created = create_product(client).json()
    payload = product_payload()
    payload.pop("unit")

    response = client.put(f"/products/{created['id']}", json=payload)

    assert response.status_code == 422


def test_put_product_returns_422_for_invalid_cost_per_unit(client):
    created = create_product(client).json()

    response = client.put(
        f"/products/{created['id']}",
        json=product_payload(cost_per_unit=-1.0),
    )

    assert response.status_code == 422


def test_put_product_returns_422_for_invalid_quantity_in_stock(client):
    created = create_product(client).json()

    response = client.put(
        f"/products/{created['id']}",
        json=product_payload(quantity_in_stock=-1.0),
    )

    assert response.status_code == 422


def test_put_product_returns_422_for_non_integer_id(client):
    response = client.put("/products/not-an-id", json=product_payload())

    assert response.status_code == 422
