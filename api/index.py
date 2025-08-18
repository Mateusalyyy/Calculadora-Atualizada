from fastapi import FastAPI
from .core.config import settings
from .database import engine
from .db_base import Base  # <-- MUDANÇA: Importa a Base do novo arquivo

from .routes import auth, users, budgets, admin, slabs

# Esta linha agora usa a Base importada de db_base.py
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stone API")

app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(budgets.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(slabs.router, prefix="/api")

@app.get("/api/health", tags=["Health Check"])
def health_check():
    return {"status": "ok"}
