# this models.py file holds all the

from pydantic import BaseModel

from bson.objectid import ObjectId

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    first_name: str
    last_name: str


class UserOutWithPassword(UserOut):
    hashed_password: str


class UserPasswordDB(UserIn):
    id: PydanticObjectId


class UserForm(BaseModel):
    username: str
    password: str


class UserToken(Token):
    account: UserOut


class HttpError(BaseModel):
    detail: str


class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: ObjectId | str) -> ObjectId:
        if value:
            try:
                ObjectId(value)
            except ValueError:
                raise ValueError(f"Not a valid object id: {value}")
        return value
