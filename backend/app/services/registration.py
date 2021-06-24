from fastapi import HTTPException

from app import crud, models
from app.db.mongodb import AsyncIOMotorClient


class RegistrationService():
    # TODO - add hashing function
    # TODO - add salt generation function
    # TODO - add flow for verifying email before you can login
    # TODO - once email is verified, allow login
    # TODO - once celery is up and running, rely on celery for portions of this flow

    async def register_new_user(self, db: AsyncIOMotorClient, obj_in: models.UserCreate) -> models.UserInDB:
        """
        Register a new user account and hash password with salt
        """
        # make sure email isn't already taken, raise exception if it is
        user = await crud.user.get_by_email(db, email=obj_in.email)
        if user:
            raise HTTPException(status_code=400, detail="Email address already in use")

        salt = 1234
        user = await crud.user.create(db, obj_in=obj_in, salt=salt)
        return user


registration = RegistrationService()