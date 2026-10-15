def create_product(product: Product):
    return product


def get_products():
    return products


def search_product(name: str, unit: str = "each"):
    filtered_products = [p for p in products if name.lower() in p.name.lower()]
    filtered_products = [p for p in filtered_products if p.unit == unit]

    return filtered_products
