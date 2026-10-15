from .schemas.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def create_product(self, product: Product):
        self.products.append(product)
        return product

    def get_products(self):
        return self.products
