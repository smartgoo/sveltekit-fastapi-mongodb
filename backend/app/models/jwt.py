from datetime import datetime, timedelta
from pydantic import EmailStr

from app.core.config import settings
from app.models.core import CoreModel


class JWTMeta(CoreModel):
    iss: str = "smartgoo.example"
    aud: str = settings.JWT_AUDIENCE
    iat: float = datetime.timestamp(datetime.utcnow())
    exp: float = datetime.timestamp(datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))


class JWTCreds(CoreModel):
    """How we'll identify users"""
    sub: EmailStr


class JWTPayload(JWTMeta, JWTCreds):
    """
    JWT Payload right before it's encoded - combine meta and username
    """
    pass


class AccessToken(CoreModel):
    access_token: str
    token_type: str
