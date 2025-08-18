from sqlalchemy.orm import Session
from ..models.slab import Slab
from ..schemas.slab import SlabCreate, SlabUpdate

def create_slab(db: Session, slab: SlabCreate):
    """
    Cria uma nova chapa no banco de dados.
    A área disponível é inicializada com a área total.
    """
    db_slab = Slab(
        name=slab.name,
        material_type=slab.material_type,
        total_area_m2=slab.total_area_m2,
        available_area_m2=slab.total_area_m2, # Regra de negócio aqui!
        price_per_m2=slab.price_per_m2
    )
    db.add(db_slab)
    db.commit()
    db.refresh(db_slab)
    return db_slab

def get_slab(db: Session, slab_id: int):
    """Busca uma única chapa pelo ID."""
    return db.query(Slab).filter(Slab.id == slab_id).first()

def get_slabs(db: Session, skip: int = 0, limit: int = 100):
    """Busca todas as chapas com paginação."""
    return db.query(Slab).offset(skip).limit(limit).all()

def update_slab(db: Session, slab_id: int, slab_update: SlabUpdate):
    """Atualiza os dados de uma chapa."""
    db_slab = get_slab(db, slab_id)
    if not db_slab:
        return None
    
    update_data = slab_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_slab, key, value)
        
    db.commit()
    db.refresh(db_slab)
    return db_slab

def delete_slab(db: Session, slab_id: int):
    """Deleta uma chapa."""
    db_slab = get_slab(db, slab_id)
    if not db_slab:
        return None
    db.delete(db_slab)
    db.commit()
    return db_slab
