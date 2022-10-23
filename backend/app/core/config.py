import secrets
import os 
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl
from databases import DatabaseURL


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # JWT Token Config
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 #7 days
    JWT_ALGORITHM: str = "HS256"
    JWT_AUDIENCE: str = "smartgoo:auth"
    JWT_TOKEN_PREFIX = "Bearer"

    SERVER_NAME: str = ''
    SERVER_HOST: str = ''

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:5173"]

    PROJECT_NAME: str = 'SvelteKit-FastAPI-MongoDB Starter Template'
    SENTRY_DSN: Optional[HttpUrl] = None

    # MongoDB config
    MONGODB_MAX_CONNECTIONS_COUNT: int = 10
    MONGODB_MIN_CONNECTIONS_COUNT: int = 10
    MONGODB_HOST: str = os.environ.get('MONGODB_HOST')
    MONGODB_PORT: int = os.environ.get('MONGODB_PORT')
    MONGODB_USER: str = os.environ.get('MONGODB_USER')
    MONGODB_PASSWORD: str = os.environ.get('MONGODB_PASSWORD')
    MONGODB_DB: str = os.environ.get('MONGODB_DB')
    MONGODB_CONN_STRING = DatabaseURL(
        f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}"
    )

    # SMTP config for sending emails
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    EMAIL_TEST_USER: EmailStr = "test@example.com"
    FIRST_SUPERUSER: EmailStr = 'test@example.com'
    FIRST_SUPERUSER_PASSWORD: str = ''
    USERS_OPEN_REGISTRATION: bool = False

    # MongodDB Collections
    USERS_COLLECTION = 'users'


    class Config:
        case_sensitive = True


settings = Settings()