from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional
from decimal import Decimal
from ..models.budget import Budget, BudgetItem, Material, AdminSetting
from ..models.user import User
from ..schemas.budget import BudgetCreate, BudgetUpdate, MaterialCreate, MaterialUpdate, AdminSettingCreate, AdminSettingUpdate
import uuid


def create_budget(db: Session, budget: BudgetCreate, user_id: uuid.UUID) -> Budget:
    """Cria um novo orçamento."""
    # Calcula o valor total dos itens
    total_amount = Decimal("0.00")
    
    db_budget = Budget(
        user_id=user_id,
        client_name=budget.client_name,
        client_contact=budget.client_contact,
        discount=budget.discount,
        taxes=budget.taxes,
        observations=budget.observations,
        total_amount=total_amount  # Será atualizado após adicionar os itens
    )
    
    db.add(db_budget)
    db.flush()  # Para obter o ID do orçamento
    
    # Adiciona os itens do orçamento
    for item_data in budget.items:
        total_item_value = item_data.quantity * item_data.unit_value
        total_amount += total_item_value
        
        db_item = BudgetItem(
            budget_id=db_budget.id,
            description=item_data.description,
            quantity=item_data.quantity,
            unit_value=item_data.unit_value,
            total_item_value=total_item_value,
            material_id=item_data.material_id
        )
        db.add(db_item)
    
    # Atualiza o valor total do orçamento
    db_budget.total_amount = total_amount - budget.discount + budget.taxes
    
    db.commit()
    db.refresh(db_budget)
    return db_budget


def get_budget(db: Session, budget_id: uuid.UUID) -> Optional[Budget]:
    """Obtém um orçamento pelo ID."""
    return db.query(Budget).filter(Budget.id == budget_id).first()


def get_budgets_by_user(db: Session, user_id: uuid.UUID, skip: int = 0, limit: int = 100) -> List[Budget]:
    """Lista orçamentos de um usuário específico."""
    return db.query(Budget).filter(Budget.user_id == user_id).offset(skip).limit(limit).all()


def get_all_budgets(db: Session, skip: int = 0, limit: int = 100) -> List[Budget]:
    """Lista todos os orçamentos (apenas para administradores)."""
    return db.query(Budget).offset(skip).limit(limit).all()


def update_budget(db: Session, budget_id: uuid.UUID, budget_update: BudgetUpdate) -> Optional[Budget]:
    """Atualiza um orçamento."""
    db_budget = db.query(Budget).filter(Budget.id == budget_id).first()
    if not db_budget:
        return None
    
    # Atualiza os campos básicos do orçamento
    update_data = budget_update.dict(exclude_unset=True, exclude={"items"})
    for field, value in update_data.items():
        setattr(db_budget, field, value)
    
    # Se há itens para atualizar, remove os antigos e adiciona os novos
    if budget_update.items is not None:
        # Remove itens existentes
        db.query(BudgetItem).filter(BudgetItem.budget_id == budget_id).delete()
        
        # Adiciona novos itens
        total_amount = Decimal("0.00")
        for item_data in budget_update.items:
            total_item_value = item_data.quantity * item_data.unit_value
            total_amount += total_item_value
            
            db_item = BudgetItem(
                budget_id=budget_id,
                description=item_data.description,
                quantity=item_data.quantity,
                unit_value=item_data.unit_value,
                total_item_value=total_item_value,
                material_id=item_data.material_id
            )
            db.add(db_item)
        
        # Atualiza o valor total
        discount = budget_update.discount if budget_update.discount is not None else db_budget.discount
        taxes = budget_update.taxes if budget_update.taxes is not None else db_budget.taxes
        db_budget.total_amount = total_amount - discount + taxes
    
    db.commit()
    db.refresh(db_budget)
    return db_budget


def delete_budget(db: Session, budget_id: uuid.UUID) -> bool:
    """Deleta um orçamento."""
    db_budget = db.query(Budget).filter(Budget.id == budget_id).first()
    if not db_budget:
        return False
    
    db.delete(db_budget)
    db.commit()
    return True


# Serviços para materiais
def create_material(db: Session, material: MaterialCreate) -> Material:
    """Cria um novo material."""
    db_material = Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def get_materials(db: Session, active_only: bool = True) -> List[Material]:
    """Lista materiais."""
    query = db.query(Material)
    if active_only:
        query = query.filter(Material.is_active == True)
    return query.all()


def update_material(db: Session, material_id: uuid.UUID, material_update: MaterialUpdate) -> Optional[Material]:
    """Atualiza um material."""
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if not db_material:
        return None
    
    update_data = material_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_material, field, value)
    
    db.commit()
    db.refresh(db_material)
    return db_material


# Serviços para configurações administrativas
def create_or_update_admin_setting(db: Session, setting: AdminSettingCreate) -> AdminSetting:
    """Cria ou atualiza uma configuração administrativa."""
    db_setting = db.query(AdminSetting).filter(AdminSetting.setting_key == setting.setting_key).first()
    
    if db_setting:
        # Atualiza configuração existente
        db_setting.setting_value = setting.setting_value
        db_setting.is_sensitive = setting.is_sensitive
    else:
        # Cria nova configuração
        db_setting = AdminSetting(**setting.dict())
        db.add(db_setting)
    
    db.commit()
    db.refresh(db_setting)
    return db_setting


def get_admin_setting(db: Session, setting_key: str) -> Optional[AdminSetting]:
    """Obtém uma configuração administrativa."""
    return db.query(AdminSetting).filter(AdminSetting.setting_key == setting_key).first()


def get_all_admin_settings(db: Session) -> List[AdminSetting]:
    """Lista todas as configurações administrativas."""
    return db.query(AdminSetting).all()

