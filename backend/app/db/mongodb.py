from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client[settings.MONGODB_DB]