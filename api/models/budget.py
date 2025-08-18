from sqlalchemy import Column, String, Text, Numeric, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from ..database import Base


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    client_name = Column(String(255), nullable=False)
    client_contact = Column(String(255), nullable=True)
    total_amount = Column(Numeric(10, 2), nullable=False)
    discount = Column(Numeric(10, 2), default=0.00)
    taxes = Column(Numeric(10, 2), default=0.00)
    observations = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relacionamentos
    user = relationship("User", back_populates="budgets")
    items = relationship("BudgetItem", back_populates="budget", cascade="all, delete-orphan")


class BudgetItem(Base):
    __tablename__ = "budget_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    budget_id = Column(UUID(as_uuid=True), ForeignKey("budgets.id"), nullable=False)
    description = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_value = Column(Numeric(10, 2), nullable=False)
    total_item_value = Column(Numeric(10, 2), nullable=False)
    material_id = Column(UUID(as_uuid=True), ForeignKey("materials.id"), nullable=True)

    # Relacionamentos
    budget = relationship("Budget", back_populates="items")
    material = relationship("Material", back_populates="budget_items")


class Material(Base):
    __tablename__ = "materials"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    unit_price = Column(Numeric(10, 2), nullable=False)
    unit_of_measure = Column(String(50), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relacionamentos
    budget_items = relationship("BudgetItem", back_populates="material")


class AdminSetting(Base):
    __tablename__ = "admin_settings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    setting_key = Column(String(255), nullable=False, unique=True)
    setting_value = Column(Text, nullable=True)
    is_sensitive = Column(Boolean, default=False, nullable=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

