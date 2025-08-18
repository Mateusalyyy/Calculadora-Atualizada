from pydantic import BaseModel
from typing import Optional

class SlabBase(BaseModel):
    name: str
    material_type: str
    total_area_m2: float
    price_per_m2: float

class SlabCreate(SlabBase):
    pass

class SlabUpdate(BaseModel):
    name: Optional[str] = None
    material_type: Optional[str] = None
    total_area_m2: Optional[float] = None
    available_area_m2: Optional[float] = None
    price_per_m2: Optional[float] = None

class Slab(SlabBase):
    id: int
    available_area_m2: float

    class Config:
        orm_mode = True
