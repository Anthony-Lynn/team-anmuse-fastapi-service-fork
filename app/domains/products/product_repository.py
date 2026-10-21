from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.domains.products.models.product_model import Product as ProductModel
from app.domains.products.schemas.product import ProductCreate, ProductUpdate


class ProductRepository:
    def create_product(self, db: Session, product: ProductCreate) -> ProductModel:
        db_product = ProductModel(
            name=product.name,
            unit=product.unit,
            cost_per_unit=product.cost_per_unit,
            price_per_unit=product.price_per_unit,
            quantity_in_stock=product.quantity_in_stock,
            category_id=product.category_id,
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return self.get_product_by_id(db, db_product.id)

    def get_products(self, db: Session) -> list[ProductModel]:
        return list(
            db.scalars(
                select(ProductModel).options(selectinload(ProductModel.category))
            ).all()
        )

    def get_product_by_id(self, db: Session, product_id: int) -> ProductModel | None:
        return db.scalars(
            select(ProductModel)
            .where(ProductModel.id == product_id)
            .options(selectinload(ProductModel.category))
        ).first()

    def update_product(
        self, db: Session, product_id: int, product: ProductUpdate
    ) -> ProductModel | None:
        db_product = self.get_product_by_id(db, product_id)
        if db_product is None:
            return None
        db_product.name = product.name
        db_product.unit = product.unit
        db_product.cost_per_unit = product.cost_per_unit
        db_product.price_per_unit = product.price_per_unit
        db_product.quantity_in_stock = product.quantity_in_stock
        db.commit()
        db.refresh(db_product)
        return self.get_product_by_id(db, product_id)

    def delete_product(self, db: Session, product_id: int) -> bool:
        db_product = self.get_product_by_id(db, product_id)
        if db_product is None:
            return False
        db.delete(db_product)
        db.commit()
        return True
