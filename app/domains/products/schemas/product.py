from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str
    unit: str
    cost_per_unit: float = Field(ge=0)
    price_per_unit: float
    quantity_in_stock: float = Field(ge=0)


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    unit: str
    price_per_unit: float
    quantity_in_stock: float
