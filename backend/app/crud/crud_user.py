from typing import Optional

from pydantic import EmailStr

from app.core.security import get_password_hash
from app.db.mongodb import AsyncIOMotorClient
from app import models


class CRUDUser():
    collection: str = 'users'

    async def get_by_email(self, db: AsyncIOMotorClient, email: EmailStr) -> Optional[models.UserInDB]:
        return await db[self.collection].find_one({"email": email})

    async def create(self, db: AsyncIOMotorClient, obj_in: models.UserCreate, salt: int) -> models.UserInDB:
        user_in = models.UserCreate(**obj_in.dict())
        user_in.password = get_password_hash(user_in.password)

        doc = await db[self.collection].insert_one({**user_in.dict(), "salt": salt})
        user_out = await db[self.collection].find_one({"_id": doc.inserted_id})

        return models.UserInDB(**user_out)

    async def update(self, db: AsyncIOMotorClient, obj_in: models.UserUpdate) -> models.UserInDB:
        # TODO
        pass

    async def delete(self, db: AsyncIOMotorClient):
        # TODO
        pass


user = CRUDUser()