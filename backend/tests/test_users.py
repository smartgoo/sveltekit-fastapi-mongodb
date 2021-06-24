import pytest

from httpx import AsyncClient
from fastapi import FastAPI

from starlette.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_400_BAD_REQUEST, 
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND, 
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from app.models.user import UserCreate, UserInDB
pytestmark = pytest.mark.asyncio

class TestUserRoutes:
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        new_user = {"email": "test@email.io", "username": "test_username", "password": "testpassword"}
        res = await client.post(app.url_path_for("users:register-new-user"), json={"new_user": new_user})
        assert res.status_code != HTTP_404_NOT_FOUND