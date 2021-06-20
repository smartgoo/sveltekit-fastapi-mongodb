from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from app.db.mongodb import db


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(str(settings.MONGODB_CONN_STRING),
                                   maxPoolSize=settings.MONGODB_MAX_CONNECTIONS_COUNT,
                                   minPoolSize=settings.MONGODB_MIN_CONNECTIONS_COUNT)


async def close_mongo_connection():
    db.client.close()
