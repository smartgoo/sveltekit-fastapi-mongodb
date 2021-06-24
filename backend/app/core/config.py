import secrets
import os 
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from databases import DatabaseURL


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = ''
    SERVER_HOST: str = ''

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://frontend"]

    PROJECT_NAME: str = 'SvelteKit FastAPI MongoDB Starter Template'
    SENTRY_DSN: Optional[HttpUrl] = None

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

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = 'test@example.com'
    FIRST_SUPERUSER_PASSWORD: str = ''
    USERS_OPEN_REGISTRATION: bool = False


    # DB Collections
    MONGODB_USERS_COLLECTION = 'users'


    class Config:
        case_sensitive = True


settings = Settings()