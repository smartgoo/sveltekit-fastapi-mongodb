from typing import Optional

from pydantic import EmailStr

from app.core.config import settings
from app.db.mongodb import AsyncIOMotorClient
from app import models


class CRUDUser():
    collection: str = settings.USERS_COLLECTION

    async def get_by_email(self, db: AsyncIOMotorClient, email: EmailStr) -> Optional[models.UserInDB]:
        user = await db[self.collection].find_one({"email": email})
        if not user:
            return None
        
        return models.UserInDB(**user)

    async def create(self, db: AsyncIOMotorClient, user_in: models.UserCreate) -> models.UserInDB:
        doc = await db[self.collection].insert_one(user_in.dict())
        user_out = await db[self.collection].find_one({"_id": doc.inserted_id})
        return models.UserInDB(**user_out)

    async def update(self, db: AsyncIOMotorClient, user_in: models.UserUpdate) -> models.UserInDB:
        # TODO
        pass

    async def delete(self, db: AsyncIOMotorClient):
        # TODO
        pass


user = CRUDUser()