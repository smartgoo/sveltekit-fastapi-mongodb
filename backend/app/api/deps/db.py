from motor.motor_asyncio import AsyncIOMotorClient

from app.db.mongodb import db
from app.core.config import settings

async def get_database() -> AsyncIOMotorClient:
    return db.client[settings.MONGODB_DB]