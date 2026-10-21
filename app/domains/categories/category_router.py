from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.domains.categories.category_service import CategoryService
from app.domains.categories.schemas.category import (
    CategoryCreate,
    CategoryResponse,
    CategoryWithProductsResponse,
)
from database import get_db

router = APIRouter()
category_service = CategoryService()


@router.post("/categories", status_code=201, response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, category)


@router.get("/categories/{category_id}", response_model=CategoryWithProductsResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = category_service.get_category_by_id(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
