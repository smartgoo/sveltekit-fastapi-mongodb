from fastapi import APIRouter, Depends, HTTPException

from app import crud, models, services
from app.db.mongodb import AsyncIOMotorClient, get_database

router = APIRouter()


@router.post('/', response_model=models.UserPublic)
async def create_user(
    obj_in: models.UserCreate,
    db: AsyncIOMotorClient = Depends(get_database),
):
    """
    Create new user
    """

    user = await services.registration.register_new_user(db, obj_in)
    return user


@router.put('/', response_model=models.UserPublic)
async def update_user(
    obj_in: models.UserUpdate,
    db: AsyncIOMotorClient = Depends(get_database)
):
    """
    Update a user
    """

    # TODO
    pass