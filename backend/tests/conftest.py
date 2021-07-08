import asyncio

from fastapi import FastAPI, Depends

import pytest
from asgi_lifespan import LifespanManager

from fastapi import FastAPI
from httpx import AsyncClient
from databases import Database

from app.db.mongodb import db
from app.api.deps.db import get_database
from app import models, services, crud
from app.core.config import settings


# Setup pytest-asyncio functions to help with closing the event loop properly. 
@pytest.fixture
def event_loop():
    yield asyncio.get_event_loop()

def pytest_sessionfinish(session, exitstatus):
    asyncio.get_event_loop().close()


# Create a new application for testing
@pytest.fixture
def app() -> FastAPI:
    def get_test_db():
        """
        Connect to a different DB just for testing
        """
        return db.client['pytest']

    from app.main import app
    app.dependency_overrides[get_database] = get_test_db
    yield app

    # Delete pytest database after tests run
    db.client.drop_database('pytest')


# Grab a reference to our database when needed
@pytest.fixture
def database(app: FastAPI) -> Database:
    return app.state._db_client['pytest']


# Make requests in our tests
@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://backend",
            headers={"Content-Type": "application/json"}
        ) as client:
            yield client


@pytest.fixture
async def test_user(database: Database) -> models.UserInDB:
    new_user = models.UserCreate(
        email="tester2@gmail.com",
        password="testtest",
        first_name="Chuck",
        last_name="Vallone"
    )
    user = await crud.user.get_by_email(db=database, email=new_user.email)
    if user:
        return user
    user = await services.registration.register_new_user(db=database, user_in=new_user)
    return user


@pytest.fixture
def authorized_client(client: AsyncClient, test_user: models.UserInDB) -> AsyncClient:
    access_token = services.authentication.create_access_token_for_user(user=test_user, secret_key=str(settings.SECRET_KEY))
    client.headers = {
        **client.headers,
        "Authorization": f"{settings.JWT_TOKEN_PREFIX} {access_token}",
    }
    return client