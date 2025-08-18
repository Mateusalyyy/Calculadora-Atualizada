from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid
import requests
import pandas as pd
from io import BytesIO

from ..database import get_db
from ..schemas.budget import AdminSetting, AdminSettingCreate, AdminSettingUpdate, MaterialCreate
from ..services.auth_service import get_current_admin_user
from ..services.budget_service import (
    create_or_update_admin_setting, get_admin_setting, get_all_admin_settings,
    create_material, get_materials
)
from ..models.user import User

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/settings", response_model=List[AdminSetting])
async def read_admin_settings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Lista todas as configurações administrativas."""
    settings = get_all_admin_settings(db)
    # Oculta valores sensíveis na resposta
    for setting in settings:
        if setting.is_sensitive and setting.setting_value:
            setting.setting_value = "***"
    return settings


@router.get("/settings/{setting_key}", response_model=AdminSetting)
async def read_admin_setting(
    setting_key: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Obtém uma configuração administrativa específica."""
    setting = get_admin_setting(db, setting_key=setting_key)
    if setting is None:
        raise HTTPException(status_code=404, detail="Configuração não encontrada")
    
    # Oculta valores sensíveis na resposta
    if setting.is_sensitive and setting.setting_value:
        setting.setting_value = "***"
    
    return setting


@router.post("/settings", response_model=AdminSetting)
async def create_or_update_admin_setting_endpoint(
    setting: AdminSettingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Cria ou atualiza uma configuração administrativa."""
    db_setting = create_or_update_admin_setting(db=db, setting=setting)
    
    # Oculta valores sensíveis na resposta
    if db_setting.is_sensitive and db_setting.setting_value:
        db_setting.setting_value = "***"
    
    return db_setting


@router.post("/sync-materials")
async def sync_materials_from_excel(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Sincroniza materiais a partir de um documento Excel configurado."""
    # Obtém a URL do Excel das configurações
    excel_url_setting = get_admin_setting(db, "EXCEL_SHEET_URL")
    if not excel_url_setting or not excel_url_setting.setting_value:
        raise HTTPException(
            status_code=400,
            detail="URL do documento Excel não configurada"
        )
    
    try:
        # Baixa o arquivo Excel
        response = requests.get(excel_url_setting.setting_value)
        response.raise_for_status()
        
        # Lê o arquivo Excel
        excel_file = BytesIO(response.content)
        df = pd.read_excel(excel_file)
        
        # Verifica se as colunas necessárias existem
        required_columns = ['nome', 'preco_unitario']
        if not all(col in df.columns for col in required_columns):
            raise HTTPException(
                status_code=400,
                detail=f"O arquivo Excel deve conter as colunas: {required_columns}"
            )
        
        # Sincroniza os materiais
        materials_created = 0
        materials_updated = 0
        
        for _, row in df.iterrows():
            material_data = MaterialCreate(
                name=str(row['nome']),
                description=str(row.get('descricao', '')),
                unit_price=float(row['preco_unitario']),
                unit_of_measure=str(row.get('unidade_medida', '')),
                is_active=bool(row.get('ativo', True))
            )
            
            # Verifica se o material já existe
            existing_materials = get_materials(db, active_only=False)
            existing_material = next(
                (m for m in existing_materials if m.name == material_data.name),
                None
            )
            
            if existing_material:
                # Atualiza material existente
                from ..services.budget_service import update_material
                from ..schemas.budget import MaterialUpdate
                
                material_update = MaterialUpdate(
                    description=material_data.description,
                    unit_price=material_data.unit_price,
                    unit_of_measure=material_data.unit_of_measure,
                    is_active=material_data.is_active
                )
                update_material(db, existing_material.id, material_update)
                materials_updated += 1
            else:
                # Cria novo material
                create_material(db, material_data)
                materials_created += 1
        
        return {
            "message": "Sincronização concluída com sucesso",
            "materials_created": materials_created,
            "materials_updated": materials_updated
        }
        
    except requests.RequestException as e:
        raise HTTPException(
            status_code=400,
            detail=f"Erro ao baixar o arquivo Excel: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar o arquivo Excel: {str(e)}"
        )


@router.get("/dashboard")
async def get_admin_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Obtém métricas para o dashboard administrativo."""
    from ..services.user_service import get_users, get_pending_users
    from ..services.budget_service import get_all_budgets
    
    # Estatísticas de usuários
    all_users = get_users(db, skip=0, limit=1000)  # Assumindo que não há mais de 1000 usuários
    pending_users = get_pending_users(db)
    active_users = [u for u in all_users if u.is_active and u.is_approved]
    
    # Estatísticas de orçamentos
    all_budgets = get_all_budgets(db, skip=0, limit=1000)  # Assumindo que não há mais de 1000 orçamentos
    
    # Valor total dos orçamentos
    total_budget_value = sum(float(budget.total_amount) for budget in all_budgets)
    
    return {
        "users": {
            "total": len(all_users),
            "active": len(active_users),
            "pending_approval": len(pending_users)
        },
        "budgets": {
            "total": len(all_budgets),
            "total_value": total_budget_value
        },
        "materials": {
            "total": len(get_materials(db, active_only=False)),
            "active": len(get_materials(db, active_only=True))
        }
    }

