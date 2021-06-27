from datetime import datetime
from typing import Optional

from pydantic import EmailStr, constr

from .jwt import AccessToken 
from app.models.core import CoreModel, DateTimeModelMixin, IDModelMixin


class UserBase(CoreModel):
    """
    Leaving off password and salt from base model
    """
    email: EmailStr
    first_name: str
    last_name: str
    email_verified: bool = False
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase, DateTimeModelMixin):
    """
    Email, password, first, last names are required for registering a new user
    """
    email: EmailStr
    password: constr(min_length=8, max_length=100)
    first_name: str
    last_name: str


class UserUpdate(UserBase):
    """
    Users are allowed to update their name and activation status
    """
    # TODO: allow user to change email address
    first_name: Optional[str]
    last_name: Optional[str]


class UserPasswordUpdate(CoreModel):
    """
    Users can change their password
    """
    password: constr(min_length=8, max_length=100)
    salt: str


class UserInDB(IDModelMixin, DateTimeModelMixin, UserBase):
    """
    Add in id, created_at, updated_at, and user's password and salt
    """
    password: constr(min_length=7, max_length=100)
    salt: str


class UserPublic(IDModelMixin, DateTimeModelMixin, UserBase):
    access_token: Optional[AccessToken]

