from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str
    unit: str
    cost_per_unit: float = Field(ge=0)
    price_per_unit: float
    quantity_in_stock: float = Field(ge=0)
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class CategoryNested(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    unit: str
    price_per_unit: float
    quantity_in_stock: float
    category: CategoryNested | None = None
