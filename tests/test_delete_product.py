from tests.conftest import create_product


def test_delete_product_returns_204_and_removes_product(client):
    created = create_product(client).json()

    response = client.delete(f"/products/{created['id']}")

    assert response.status_code == 204
    assert response.content == b""
    assert client.get(f"/products/{created['id']}").status_code == 404
    assert client.get("/products").json() == []


def test_delete_product_returns_404_when_missing(client):
    response = client.delete("/products/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "No product found"


def test_delete_product_twice_returns_404_on_second_call(client):
    created = create_product(client).json()

    first = client.delete(f"/products/{created['id']}")
    second = client.delete(f"/products/{created['id']}")

    assert first.status_code == 204
    assert second.status_code == 404


def test_delete_product_returns_422_for_non_integer_id(client):
    response = client.delete("/products/not-an-id")

    assert response.status_code == 422
