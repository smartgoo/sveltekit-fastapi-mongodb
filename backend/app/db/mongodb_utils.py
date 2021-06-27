from fastapi import FastAPI

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.db.mongodb import db


def connect_to_mongo(app: FastAPI):
    print('connecting to database')
    db.client = AsyncIOMotorClient(str(settings.MONGODB_CONN_STRING),
                                   maxPoolSize=settings.MONGODB_MAX_CONNECTIONS_COUNT,
                                   minPoolSize=settings.MONGODB_MIN_CONNECTIONS_COUNT)
    app.state._db_client = db.client
    print('connected')


def close_mongo_connection(app: FastAPI):
    print('closing database connection')
    db.client.close()
    print('closed')
