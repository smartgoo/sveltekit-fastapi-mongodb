from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import status

from app import crud, models, services
from app.db.mongodb import AsyncIOMotorClient
from app.api.deps.db import get_database
from app.api.deps.auth import get_current_active_user


router = APIRouter()


@router.post('/', name="user:create", response_model=models.UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user(
    obj_in: models.UserCreate,
    db: AsyncIOMotorClient = Depends(get_database),
):
    """
    Create new user
    """
    obj_in = models.UserCreate(**obj_in.dict())
    user = await services.registration.register_new_user(db, obj_in)
    access_token = models.AccessToken(
        access_token = services.authentication.create_access_token_for_user(user=user), token_type="bearer"
    )
    return models.UserPublic(**user.dict(), access_token=access_token)


@router.post('/login/token', name="user:login", response_model=models.AccessToken)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    db: AsyncIOMotorClient = Depends(get_database),
) -> models.AccessToken:
    """
    Authentication endpoint
    """
    token = await services.authentication.authenticate_user(db=db, email=form_data.username, password=form_data.password)
    return token


@router.get("/me/", response_model=models.UserPublic, name="user:me")
async def get_currently_authenticated_user(current_user: models.UserInDB = Depends(get_current_active_user)) -> models.UserPublic:
    """
    Get current user
    """
    return current_user