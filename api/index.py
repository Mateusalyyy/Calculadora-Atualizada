print("--- INICIANDO api/index.py ---")

try:
    print("[1/5] Importando FastAPI...")
    from fastapi import FastAPI
    
    print("[2/5] Importando configurações e Base do DB...")
    from .core.config import settings
    from .database import engine
    from .db_base import Base
    
    print("[3/5] Importando roteadores...")
    from .routes import auth, users, budgets, admin, slabs

    print("[4/5] Criando tabelas no banco de dados (Base.metadata.create_all)...")
    Base.metadata.create_all(bind=engine)
    print("...Tabelas criadas com sucesso (ou já existiam).")

    print("[5/5] Criando a instância do FastAPI...")
    app = FastAPI(title="Stone API")

    app.include_router(auth.router, prefix="/api")
    app.include_router(users.router, prefix="/api")
    app.include_router(budgets.router, prefix="/api")
    app.include_router(admin.router, prefix="/api")
    app.include_router(slabs.router, prefix="/api")

    @app.get("/api/health", tags=["Health Check"])
    def health_check():
        return {"status": "ok"}
    
    print("--- APLICAÇÃO INICIADA COM SUCESSO ---")

except Exception as e:
    print("!!!!!! OCORREU UM ERRO DURANTE A INICIALIZAÇÃO !!!!!!")
    print(f"Erro: {e}")
    import traceback
    traceback.print_exc()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # Lança o erro novamente para que o Render saiba que falhou
    raise e
