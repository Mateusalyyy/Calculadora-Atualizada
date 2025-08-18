from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, services
from ..database import get_db

router = APIRouter(
    prefix="/slabs",
    tags=["Slabs"]
)

@router.post("/", response_model=schemas.Slab)
def create_new_slab(slab: schemas.SlabCreate, db: Session = Depends(get_db)):
    """Endpoint para criar uma nova chapa no estoque."""
    return services.slab_service.create_slab(db=db, slab=slab)

@router.get("/", response_model=List[schemas.Slab])
def read_all_slabs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Endpoint para listar todas as chapas. A calculadora usará este."""
    slabs = services.slab_service.get_slabs(db, skip=skip, limit=limit)
    return slabs

@router.get("/{slab_id}", response_model=schemas.Slab)
def read_single_slab(slab_id: int, db: Session = Depends(get_db)):
    """Endpoint para buscar uma chapa específica."""
    db_slab = services.slab_service.get_slab(db, slab_id=slab_id)
    if db_slab is None:
        raise HTTPException(status_code=404, detail="Slab not found")
    return db_slab

@router.put("/{slab_id}", response_model=schemas.Slab)
def update_existing_slab(slab_id: int, slab_update: schemas.SlabUpdate, db: Session = Depends(get_db)):
    """Endpoint para atualizar uma chapa."""
    db_slab = services.slab_service.update_slab(db, slab_id=slab_id, slab_update=slab_update)
    if db_slab is None:
        raise HTTPException(status_code=404, detail="Slab not found")
    return db_slab

@router.delete("/{slab_id}", response_model=schemas.Slab)
def delete_existing_slab(slab_id: int, db: Session = Depends(get_db)):
    """Endpoint para deletar uma chapa."""
    db_slab = services.slab_service.delete_slab(db, slab_id=slab_id)
    if db_slab is None:
        raise HTTPException(status_code=404, detail="Slab not found")
    return db_slab
