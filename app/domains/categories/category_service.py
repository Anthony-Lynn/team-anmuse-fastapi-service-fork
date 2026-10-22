from sqlalchemy.orm import Session

from app.domains.categories.category_repository import CategoryRepository
from app.domains.categories.models.category_model import Category as CategoryModel
from app.domains.categories.schemas.category import CategoryCreate


class CategoryService:
    def __init__(self, repository: CategoryRepository | None = None):
        self.repository = repository or CategoryRepository()

    def create_category(self, db: Session, category: CategoryCreate) -> CategoryModel:
        return self.repository.create_category(db, category)

    def get_category_by_id(self, db: Session, category_id: int) -> CategoryModel | None:
        return self.repository.get_category_by_id(db, category_id)

    def category_exists(self, db: Session, category_id: int | None) -> bool:
        if category_id is None:
            return True  # no category given, so there's nothing to check
        return self.repository.get_category_by_id(db, category_id) is not None