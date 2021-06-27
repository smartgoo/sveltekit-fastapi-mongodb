from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.db.mongodb import db

async def get_database() -> AsyncIOMotorClient:
    return db.client[settings.MONGODB_DB]