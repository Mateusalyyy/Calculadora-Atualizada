from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .core.config import settings

# --- Ponto Central de Importação dos Modelos ---
# Ao importar todos os modelos aqui, garantimos que o SQLAlchemy
# "enxergue" todos eles quando for criar as tabelas no banco de dados.
from .models.user import User
from .models.budget import Budget
from .models.slab import Slab  # <-- ADICIONADO: O novo modelo de Chapa

# --- Configuração da Conexão com o Banco de Dados ---
# A lógica para lidar com SQLite vs. outros bancos de dados já está correta.
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {}
)

# Cria uma fábrica de sessões que será usada para interagir com o banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base da qual todos os modelos de tabela irão herdar.
Base = declarative_base()


def get_db():
    """
    Função de Dependência (Dependency) para o FastAPI.
    
    Esta função cria uma nova sessão do banco de dados para cada requisição
    que chega na API, garante que a sessão seja fechada ao final, mesmo que
    um erro ocorra, e disponibiliza a sessão para as rotas.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

