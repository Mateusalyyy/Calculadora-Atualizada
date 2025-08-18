from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    admin_email: str
    admin_password: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()

# --- LOGS DE DEPURAÇÃO ---
print("--- CONFIGURAÇÕES CARREGADAS ---")
print(f"DATABASE_URL: ...{settings.database_url[-10:]}") # Imprime só o final por segurança
print(f"SECRET_KEY: {'*' * len(settings.secret_key)}")
print(f"ALGORITHM: {settings.algorithm}")
print(f"ADMIN_EMAIL: {settings.admin_email}")
print("---------------------------------")
