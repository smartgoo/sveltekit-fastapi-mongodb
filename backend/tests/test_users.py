from typing import List, Union, Type, Optional

import pytest
import jwt
from httpx import AsyncClient
from fastapi import FastAPI
from databases import Database
from pydantic import ValidationError
from starlette.datastructures import Secret
from starlette.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_400_BAD_REQUEST, 
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND, 
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from app import models, services, crud
from app.core.config import settings



class TestUserRoutes:
    @pytest.mark.asyncio
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("user:create"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND
    

class TestUserRegistration:
    @pytest.mark.asyncio
    async def test_successful_user_create(self, app: FastAPI, client: AsyncClient) -> None:
        body = {
            "email": "test@gmail.com",
            "password": "testtest",
            "first_name": "Charles",
            "last_name": "Vallone"
        }
        res = await client.post(app.url_path_for("user:create"), json=body)
        assert res.status_code == HTTP_201_CREATED
        data = res.json()
        assert type(models.UserPublic(**data)) is models.UserPublic
        

    @pytest.mark.asyncio
    async def test_invalid_create_input_raises_error(self, app: FastAPI, client: AsyncClient) -> None:
        body_no_password = {
            "email": "test@gmail.com",
            "first_name": "Charles",
            "last_name": "Vallone"
        }
        res = await client.post(app.url_path_for("user:create"), json=body_no_password)
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY

        body_no_email = {
            "password": "testtest",
            "first_name": "Charles",
            "last_name": "Vallone"
        }
        res = await client.post(app.url_path_for("user:create"), json=body_no_email)
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY

        body_no_first = {
            "email": "test@gmail.com",
            "password": "testtest",
            "last_name": "Vallone"
        }
        res = await client.post(app.url_path_for("user:create"), json=body_no_first)
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY


        body_no_last = {
            "email": "test@gmail.com",
            "password": "testtest",
            "first_name": "Charles"
        }
        res = await client.post(app.url_path_for("user:create"), json=body_no_last)
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY


    @pytest.mark.asyncio
    async def test_email_already_in_use(self, app: FastAPI, client: AsyncClient) -> None:
        body = {
            "email": "test-duplicate@gmail.com",
            "password": "testtest",
            "first_name": "Charles",
            "last_name": "Vallone"
        }

        # Create it the first time
        res = await client.post(app.url_path_for("user:create"), json=body)
        assert res.status_code == HTTP_201_CREATED

        # Try to create it again
        res = await client.post(app.url_path_for("user:create"), json=body)
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY
        assert res.json()['detail'] == "Email address already in use"

    @pytest.mark.asyncio
    async def test_users_saved_password_is_hashed_and_has_salt(
        self,
        app: FastAPI,
        client: AsyncClient,
        database: Database
    ) -> None:

        body = {
            "email": "test@gmail.com",
            "password": "testtest",
            "first_name": "Charles",
            "last_name": "Vallone"
        }

        # send post request to create user and ensure it is successful
        res = await client.post(app.url_path_for("user:create"), json=body)
        assert res.status_code == HTTP_201_CREATED

        # ensure that the users password is hashed in the db
        # and that we can verify it using our auth service
        user_in_db = await crud.user.get_by_email(db=database, email=body["email"])
        print(type(user_in_db))
        print(user_in_db.salt)
        assert user_in_db is not None
        assert user_in_db.salt is not None and user_in_db.salt != "123"        
        assert user_in_db.password != body["password"]
        assert services.authentication.verify_password(
            password=body["password"], 
            salt=user_in_db.salt, 
            hashed_password=user_in_db.password,
        )


class TestAuthTokens:
    @pytest.mark.asyncio
    async def test_can_successfully_create_access_token(
        self, app: FastAPI, client: AsyncClient, test_user: models.UserInDB
    ) -> None:
        access_token = services.authentication.create_access_token_for_user(
            user=test_user,
            secret_key=str(settings.SECRET_KEY),
            audience=settings.JWT_AUDIENCE,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )

        creds = jwt.decode(access_token, str(settings.SECRET_KEY), audience=settings.JWT_AUDIENCE, algorithms=[settings.JWT_ALGORITHM])
        print(creds)
        assert creds.get("sub") is not None
        assert creds["sub"] == test_user.email
        assert creds["aud"] == settings.JWT_AUDIENCE


    @pytest.mark.asyncio
    async def test_token_missing_user_is_invalid(self, app: FastAPI, client: AsyncClient) -> None:
        access_token = services.authentication.create_access_token_for_user(
            user=None,
            secret_key=str(settings.SECRET_KEY),
            audience=settings.JWT_AUDIENCE,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )

        with pytest.raises(jwt.PyJWTError):
            jwt.decode(access_token, str(settings.SECRET_KEY), audience=settings.JWT_AUDIENCE, algorithms=[settings.JWT_ALGORITHM])


    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "secret_key, jwt_audience, exception",
        (
            ("wrong-secret", settings.JWT_AUDIENCE, jwt.InvalidSignatureError),
            (None, settings.JWT_AUDIENCE, jwt.InvalidSignatureError),
            (settings.SECRET_KEY, "othersite:auth", jwt.InvalidAudienceError),
            (settings.SECRET_KEY, None, ValidationError),
        )
    )
    async def test_invalid_token_content_raises_error(
        self,
        app: FastAPI,
        client: AsyncClient,
        database: Database,
        secret_key: Union[str, Secret],
        jwt_audience: str,
        exception: Type[BaseException],
        test_user: models.UserInDB
    ) -> None:
        
        with pytest.raises(exception):
            access_token = services.authentication.create_access_token_for_user(
                user=test_user,
                secret_key=str(secret_key),
                audience=jwt_audience,
                expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
            )
            print(access_token)

            jwt.decode(access_token, str(settings.SECRET_KEY), audience=settings.JWT_AUDIENCE, algorithms=[settings.JWT_ALGORITHM])


class TestUserLogin:
    @pytest.mark.asyncio
    async def test_user_can_login_successfully_and_receives_valid_token(
        self, app: FastAPI, client: AsyncClient, test_user: models.UserInDB,
    ) -> None:
        client.headers["content-type"] = "application/x-www-form-urlencoded"
        login_data = {
            "username": test_user.email,
            "password": "testtest",  # insert user's plaintext password
        }
        res = await client.post(app.url_path_for("user:login"), data=login_data)
        assert res.status_code == HTTP_200_OK

        # check that token exists in response and has user encoded within it
        token = res.json().get("access_token")
        creds = jwt.decode(token, str(settings.SECRET_KEY), audience=settings.JWT_AUDIENCE, algorithms=[settings.JWT_ALGORITHM])
        print(creds)
        # assert "email" in creds # TODO - this is failing. why don't I have email address in here? Had to chagne this in another test to `sub` to get that to work. Is it an issue if email is not in here
        # assert creds["email"] == test_user.username
        assert "sub" in creds
        assert creds["sub"] == test_user.email

        # check that token is proper type
        assert "token_type" in res.json()
        assert res.json().get("token_type") == "bearer"


#     @pytest.mark.parametrize(
#         "credential, wrong_value, status_code",
#         (
#             ("email", "wrong@email.com", 401),
#             ("email", None, 401),
#             ("email", "notemail", 401),
#             ("password", "wrongpassword", 401),
#             ("password", None, 401),
#         ),
#     )
#     async def test_user_with_wrong_creds_doesnt_receive_token(
#         self,
#         app: FastAPI,
#         client: AsyncClient,
#         test_user: models.UserInDB,
#         credential: str,
#         wrong_value: str,
#         status_code: int,
#     ) -> None:
#         client.headers["content-type"] = "application/x-www-form-urlencoded"
#         user_data = test_user.dict()
#         user_data["password"] = "testtest"  # insert user's plaintext password
#         user_data[credential] = wrong_value
#         login_data = {
#             "username": user_data["email"],
#             "password": user_data["password"],  # insert password from parameters
#         }
#         res = await client.post(app.url_path_for("users:login-email-and-password"), data=login_data)
#         assert res.status_code == status_code
#         assert "access_token" not in res.json()