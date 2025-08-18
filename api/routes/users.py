from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from ..database import get_db
from ..schemas.user import User, UserUpdate
from ..services.auth_service import get_current_user, get_current_admin_user
from ..services.user_service import (
    get_user, get_users, get_pending_users, update_user, 
    approve_user, deactivate_user, delete_user
)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Obtém informações do usuário atual."""
    return current_user


@router.get("/", response_model=List[User])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Lista todos os usuários (apenas administradores)."""
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/pending", response_model=List[User])
async def read_pending_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Lista usuários pendentes de aprovação (apenas administradores)."""
    users = get_pending_users(db)
    return users


@router.get("/{user_id}", response_model=User)
async def read_user(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Obtém um usuário específico (apenas administradores)."""
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.put("/{user_id}", response_model=User)
async def update_user_endpoint(
    user_id: uuid.UUID,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Atualiza um usuário (apenas administradores)."""
    db_user = update_user(db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.post("/{user_id}/approve", response_model=User)
async def approve_user_endpoint(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Aprova um usuário (apenas administradores)."""
    db_user = approve_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.post("/{user_id}/deactivate", response_model=User)
async def deactivate_user_endpoint(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Desativa um usuário (apenas administradores)."""
    db_user = deactivate_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


@router.delete("/{user_id}")
async def delete_user_endpoint(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Deleta um usuário (apenas administradores)."""
    success = delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}

