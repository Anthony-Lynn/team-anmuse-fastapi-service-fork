from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.domains.categories.models.category_model import Category as CategoryModel
from app.domains.categories.schemas.category import CategoryCreate


class CategoryRepository:
    def create_category(self, db: Session, category: CategoryCreate) -> CategoryModel:
        db_category = CategoryModel(name=category.name)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category

    def get_category_by_id(self, db: Session, category_id: int) -> CategoryModel | None:
        return db.scalars(
            select(CategoryModel)
            .where(CategoryModel.id == category_id)
            .options(selectinload(CategoryModel.products))
        ).first()
