from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.db.mongodb import db
from app import services, models, crud
from .db import get_database


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/users/login/token/")


async def get_user_from_token(
    token: str = Depends(oauth2_scheme),
    db: AsyncIOMotorClient = Depends(get_database),
) -> Optional[models.UserInDB]:
    try:
        email = services.authentication.get_email_from_token(token=token, secret_key=str(settings.SECRET_KEY))
        user = await crud.user.get_by_email(db=db, email=email)
    except Exception as e:
        raise e
    return user


def get_current_active_user(current_user: models.UserInDB = Depends(get_user_from_token)) -> Optional[models.UserInDB]:
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="No authenticated user.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Not an active user.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user
