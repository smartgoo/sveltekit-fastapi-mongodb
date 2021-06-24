from bson.objectid import ObjectId

class MongoIDType(ObjectId):
    """
    A custom type for MongoDB. Refer to this repo:
    https://github.com/mongodb-developer/mongodb-with-fastapi
    https://developer.mongodb.com/quickstart/python-quickstart-fastapi/
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")