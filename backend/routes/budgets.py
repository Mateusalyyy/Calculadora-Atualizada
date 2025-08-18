from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from ..database import get_db
from ..schemas.budget import Budget, BudgetCreate, BudgetUpdate, Material, MaterialCreate, MaterialUpdate
from ..services.auth_service import get_current_user, get_current_admin_user
from ..services.budget_service import (
    create_budget, get_budget, get_budgets_by_user, get_all_budgets,
    update_budget, delete_budget, create_material, get_materials, update_material
)
from ..models.user import User

router = APIRouter(prefix="/budgets", tags=["budgets"])


@router.post("/", response_model=Budget)
async def create_budget_endpoint(
    budget: BudgetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Cria um novo orçamento."""
    return create_budget(db=db, budget=budget, user_id=current_user.id)


@router.get("/", response_model=List[Budget])
async def read_budgets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Lista orçamentos do usuário atual ou todos (se administrador)."""
    if current_user.role == "administrador":
        budgets = get_all_budgets(db, skip=skip, limit=limit)
    else:
        budgets = get_budgets_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
    return budgets


@router.get("/{budget_id}", response_model=Budget)
async def read_budget(
    budget_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Obtém um orçamento específico."""
    db_budget = get_budget(db, budget_id=budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Orçamento não encontrado")
    
    # Verifica se o usuário tem permissão para ver este orçamento
    if current_user.role != "administrador" and db_budget.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado a este orçamento"
        )
    
    return db_budget


@router.put("/{budget_id}", response_model=Budget)
async def update_budget_endpoint(
    budget_id: uuid.UUID,
    budget_update: BudgetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Atualiza um orçamento."""
    db_budget = get_budget(db, budget_id=budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Orçamento não encontrado")
    
    # Verifica se o usuário tem permissão para editar este orçamento
    if current_user.role != "administrador" and db_budget.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado para editar este orçamento"
        )
    
    updated_budget = update_budget(db, budget_id=budget_id, budget_update=budget_update)
    return updated_budget


@router.delete("/{budget_id}")
async def delete_budget_endpoint(
    budget_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Deleta um orçamento."""
    db_budget = get_budget(db, budget_id=budget_id)
    if db_budget is None:
        raise HTTPException(status_code=404, detail="Orçamento não encontrado")
    
    # Verifica se o usuário tem permissão para deletar este orçamento
    if current_user.role != "administrador" and db_budget.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado para deletar este orçamento"
        )
    
    success = delete_budget(db, budget_id=budget_id)
    if not success:
        raise HTTPException(status_code=404, detail="Orçamento não encontrado")
    return {"message": "Orçamento deletado com sucesso"}


# Rotas para materiais
@router.get("/materials/", response_model=List[Material])
async def read_materials(
    active_only: bool = True,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Lista materiais disponíveis."""
    materials = get_materials(db, active_only=active_only)
    return materials


@router.post("/materials/", response_model=Material)
async def create_material_endpoint(
    material: MaterialCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Cria um novo material (apenas administradores)."""
    return create_material(db=db, material=material)


@router.put("/materials/{material_id}", response_model=Material)
async def update_material_endpoint(
    material_id: uuid.UUID,
    material_update: MaterialUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Atualiza um material (apenas administradores)."""
    db_material = update_material(db, material_id=material_id, material_update=material_update)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    return db_material

