from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional
from ..models.user import User, UserRole
from ..schemas.user import UserCreate, UserUpdate
from ..core.security import get_password_hash
import uuid


def create_user(db: Session, user: UserCreate) -> User:
    """Cria um novo usuário."""
    # Verifica se o username já existe
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nome de usuário já existe"
        )
    
    # Verifica se o email já existe
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já está em uso"
        )
    
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: uuid.UUID) -> Optional[User]:
    """Obtém um usuário pelo ID."""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """Obtém um usuário pelo username."""
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Obtém um usuário pelo email."""
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """Lista todos os usuários."""
    return db.query(User).offset(skip).limit(limit).all()


def get_pending_users(db: Session) -> List[User]:
    """Lista usuários pendentes de aprovação."""
    return db.query(User).filter(User.is_approved == False).all()


def update_user(db: Session, user_id: uuid.UUID, user_update: UserUpdate) -> Optional[User]:
    """Atualiza um usuário."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user


def approve_user(db: Session, user_id: uuid.UUID) -> Optional[User]:
    """Aprova um usuário."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    db_user.is_approved = True
    db.commit()
    db.refresh(db_user)
    return db_user


def deactivate_user(db: Session, user_id: uuid.UUID) -> Optional[User]:
    """Desativa um usuário."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: uuid.UUID) -> bool:
    """Deleta um usuário."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return False
    
    db.delete(db_user)
    db.commit()
    return True

