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
    """
    Allows a model to read the MongoDB _id in
    TODO figure out better way to handle this
    """
    id: MongoIDType = Field(alias='_id')

    class Config:
        # Allows `id` or `_id` input to popluate the field `id`
        allow_population_by_field_name = True 

        # Allows use of our custom type `MongoIDType`
        arbitrary_types_allowed = True

        # Since MongoDB ObjectIDs are BSON, this allows encoding to JSON
        json_encoders = {ObjectId: str}