from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from .core.config import settings
from .database import engine, Base
from .routes import auth, users, budgets, admin

# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Budget Calculator SaaS",
    description="Plataforma SaaS para Calculadora de Orçamentos",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas da API
app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(budgets.router, prefix="/api")
app.include_router(admin.router, prefix="/api")

# Serve arquivos estáticos do frontend
frontend_path = os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "build")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path + "/static"), name="static")
    
    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        """Serve o frontend React para todas as rotas não-API."""
        if full_path.startswith("api/"):
            return {"error": "API endpoint not found"}
        
        file_path = os.path.join(frontend_path, full_path)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        else:
            # Retorna o index.html para rotas do React Router
            return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/")
async def root():
    """Endpoint raiz da API."""
    if os.path.exists(frontend_path):
        return FileResponse(os.path.join(frontend_path, "index.html"))
    else:
        return {
            "message": "Budget Calculator SaaS API",
            "version": "1.0.0",
            "docs": "/docs"
        }

@app.get("/health")
async def health_check():
    """Endpoint para verificação de saúde da aplicação."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

