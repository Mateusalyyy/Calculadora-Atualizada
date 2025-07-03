from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite:///./budget_calculator.db"
    
    # Security
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS
    allowed_origins: list = ["*"]
    
    # Admin
    admin_email: str = "admin@example.com"
    admin_password: str = "admin123"
    
    # Environment
    environment: str = "development"
    
    class Config:
        env_file = ".env"


settings = Settings()

