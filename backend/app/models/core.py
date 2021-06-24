from typing import Optional
from datetime import datetime

from bson.objectid import ObjectId
from pydantic import BaseModel, Field, validator

from app.core.extras.typehints import MongoIDType


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """
    pass


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.now()


class IDModelMixin(BaseModel):
    id: MongoIDType = Field(alias='_id')

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}