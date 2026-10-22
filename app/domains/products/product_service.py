
from sqlalchemy.orm import Session

from app.domains.categories.category_service import CategoryService
from app.domains.products.models.product_model import Product as ProductModel
from app.domains.products.product_repository import ProductRepository
from app.domains.products.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(
        self,
        repository: ProductRepository | None = None,
        category_service: CategoryService | None = None,
    ):
        self.repository = repository or ProductRepository()
        self.category_service = category_service or CategoryService()

    def create_product(self, db: Session, product: ProductCreate) -> ProductModel:
        # self.category_service._ensure_category_exists(db, product.category_id)
        return self.repository.create_product(db, product)

    def get_products(self, db: Session) -> list[ProductModel]:
        return self.repository.get_products(db)

    def get_product_by_id(self, db: Session, product_id: int) -> ProductModel | None:
        return self.repository.get_product_by_id(db, product_id)

    def update_product(
        self, db: Session, product_id: int, product: ProductUpdate
    ) -> ProductModel | None:
        if self.repository.get_product_by_id(db, product_id) is None:
            return None
        self.category_service.ensure_category_exists(db, product.category_id)
        return self.repository.update_product(db, product_id, product)

    def delete_product(self, db: Session, product_id: int) -> bool:
        return self.repository.delete_product(db, product_id)

    def search_product(
        self, db: Session, name: str, unit: str = "each"
    ) -> list[ProductModel]:
        products = self.repository.get_products(db)
        filtered_products = [p for p in products if name.lower() in p.name.lower()]
        filtered_products = [p for p in filtered_products if p.unit == unit]
        return filtered_products