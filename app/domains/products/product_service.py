from .product_repository import ProductRepository
from .schemas.product import Product


class ProductService:
    def __init__(self, repository: ProductRepository | None = None):
        self.repository = repository or ProductRepository()

    def create_product(self, product: Product):
        return self.repository.create_product(product)

    def get_products(self):
        return self.repository.get_products()

    def search_product(self, name: str, unit: str = "each"):
        products = self.repository.get_products()
        filtered_products = [p for p in products if name.lower() in p.name.lower()]
        filtered_products = [p for p in filtered_products if p.unit == unit]

        return filtered_products
