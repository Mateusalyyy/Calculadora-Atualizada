from fastapi import FastAPI
from .core.config import settings
from .database import engine, Base

# --- Ponto Central de Importação das Rotas ---
from .routes import auth, users, budgets, admin
from .routes import slabs  # <-- ADICIONADO: O novo roteador de Chapas

# --- Criação das Tabelas no Banco de Dados ---
# Esta linha é crucial. Ela instrui o SQLAlchemy a criar todas as tabelas
# que foram importadas através do database.py (Users, Budgets, Slabs, etc.)
# assim que a aplicação inicia.
Base.metadata.create_all(bind=engine)


# --- Instância Principal da Aplicação FastAPI ---
app = FastAPI(
    title="Stone API",
    description="API para o sistema de gestão de marmorarias Stone.",
    version="1.0.0",
    # A URL do /docs é gerada automaticamente, não precisa de configuração extra.
)


# --- Inclusão dos Roteadores da API ---
# Cada "módulo" da nossa API (autenticação, usuários, estoque) é
# registrado aqui. O prefixo "/api" garante que todas as nossas rotas
# comecem com /api/... (ex: /api/users/, /api/slabs/).
app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(budgets.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(slabs.router, prefix="/api") # <-- ADICIONADO: Registra as rotas de estoque


# --- Endpoint de Verificação de Saúde (Health Check) ---
# É uma boa prática ter um endpoint simples para verificar se a API
# está no ar e respondendo.
@app.get("/api/health", tags=["Health Check"])
def health_check():
    """Verifica se a API está operacional."""
    return {"status": "ok", "version": app.version}

