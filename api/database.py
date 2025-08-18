from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .core.config import settings
from .db_base import Base  # <-- MUDANÇA 1: Importa a Base do novo arquivo

# Importa os modelos para que a Base os reconheça
from .models.user import User
from .models.budget import Budget
from .models.slab import Slab

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A linha "Base = declarative_base()" foi REMOVIDA daqui.

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
