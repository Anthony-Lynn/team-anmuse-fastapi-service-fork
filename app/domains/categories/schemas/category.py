from pydantic import BaseModel, ConfigDict

from app.domains.products.schemas.product import ProductResponse


class CategoryCreate(BaseModel):
    name: str


class CategorySummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class CategoryWithProductsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    products: list[ProductResponse]
