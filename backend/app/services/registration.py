from fastapi import HTTPException

from app import crud, models, services
from app.db.mongodb import AsyncIOMotorClient


class RegistrationService():
    """
    An API to handle user registration.
    Abstracts out the lower level operations in the registration flow.
    Handles crud operations, celery worker delegation, emails, etc.
    """
    # TODO - add hashing function
    # TODO - add salt generation function
    # TODO - add flow for verifying email before you can login
    # TODO - once email is verified, allow login
    # TODO - once celery is up and running, rely on celery for portions of this flow

    async def register_new_user(self, db: AsyncIOMotorClient, user_in: models.UserCreate) -> models.UserInDB:
        """
        Register a new user account and hash password with salt
        """
        # make sure email isn't already taken, raise exception if it is
        user = await crud.user.get_by_email(db, email=user_in.email)
        if user:
            raise HTTPException(status_code=422, detail="Email address already in use")

        user_password_update = services.authentication.create_salt_and_hashed_password(plaintext_password=user_in.password)
        new_user_params = user_in.copy(update=user_password_update.dict())
        user = await crud.user.create(db, user_in=new_user_params)
        return user


registration = RegistrationService()