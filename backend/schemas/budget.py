from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal
import uuid


class BudgetItemBase(BaseModel):
    description: str
    quantity: int
    unit_value: Decimal
    material_id: Optional[uuid.UUID] = None


class BudgetItemCreate(BudgetItemBase):
    pass


class BudgetItemUpdate(BudgetItemBase):
    description: Optional[str] = None
    quantity: Optional[int] = None
    unit_value: Optional[Decimal] = None


class BudgetItemInDB(BudgetItemBase):
    id: uuid.UUID
    budget_id: uuid.UUID
    total_item_value: Decimal

    class Config:
        from_attributes = True


class BudgetItem(BudgetItemInDB):
    pass


class BudgetBase(BaseModel):
    client_name: str
    client_contact: Optional[str] = None
    discount: Decimal = Decimal("0.00")
    taxes: Decimal = Decimal("0.00")
    observations: Optional[str] = None


class BudgetCreate(BudgetBase):
    items: List[BudgetItemCreate]


class BudgetUpdate(BaseModel):
    client_name: Optional[str] = None
    client_contact: Optional[str] = None
    discount: Optional[Decimal] = None
    taxes: Optional[Decimal] = None
    observations: Optional[str] = None
    items: Optional[List[BudgetItemCreate]] = None


class BudgetInDB(BudgetBase):
    id: uuid.UUID
    user_id: uuid.UUID
    total_amount: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Budget(BudgetInDB):
    items: List[BudgetItem] = []


class MaterialBase(BaseModel):
    name: str
    description: Optional[str] = None
    unit_price: Decimal
    unit_of_measure: Optional[str] = None
    is_active: bool = True


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    unit_price: Optional[Decimal] = None
    unit_of_measure: Optional[str] = None
    is_active: Optional[bool] = None


class MaterialInDB(MaterialBase):
    id: uuid.UUID
    last_updated: datetime

    class Config:
        from_attributes = True


class Material(MaterialInDB):
    pass


class AdminSettingBase(BaseModel):
    setting_key: str
    setting_value: Optional[str] = None
    is_sensitive: bool = False


class AdminSettingCreate(AdminSettingBase):
    pass


class AdminSettingUpdate(BaseModel):
    setting_value: Optional[str] = None
    is_sensitive: Optional[bool] = None


class AdminSettingInDB(AdminSettingBase):
    id: uuid.UUID
    last_updated: datetime

    class Config:
        from_attributes = True


class AdminSetting(AdminSettingInDB):
    pass

