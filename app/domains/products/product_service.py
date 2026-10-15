from app.domains.products.schemas.product import Product


class ProductService:
    def __init__(self):
        self.products: list[Product] = []

    def create_product(self, product: Product):
        self.products.append(product)
        return product

    def get_products(self):
        return self.products

    def search_product(self, name: str, unit: str = "each"):
        filtered_products = [p for p in self.products if name.lower() in p.name.lower()]
        filtered_products = [p for p in filtered_products if p.unit == unit]

        return filtered_products
