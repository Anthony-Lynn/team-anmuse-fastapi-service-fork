from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domains.products.models.product_model import Product as ProductModel
from app.domains.products.schemas.product import ProductCreate


class ProductRepository:
    def create_product(self, db: Session, product: ProductCreate) -> ProductModel:
        db_product = ProductModel(
            name=product.name,
            unit=product.unit,
            cost_per_unit=product.cost_per_unit,
            price_per_unit=product.price_per_unit,
            quantity_in_stock=product.quantity_in_stock,
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def get_products(self, db: Session) -> list[ProductModel]:
        return list(db.scalars(select(ProductModel)).all())

    def get_product_by_id(self, db: Session, product_id: int) -> ProductModel | None:
        return db.get(ProductModel, product_id)
