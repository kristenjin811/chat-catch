# this models.py file holds all the models.
# commented models/imports are not used yet or might be deleted

# from fastapi import Response
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from datetime import datetime

# user models
# message models
# chatroom models
# auth models
# misc models


# USER MODELS
class User(BaseModel):
    username: str
    # hashed_password: str
    # salt: str
    # profile_pic_img_src: Optional[str]
    # favorites: List[str] = []
    # disabled: bool = False


class UserInDB(User):
    _id: ObjectId
    date_created: datetime = Field(default_factory=datetime.utcnow)


# MESSAGE MODELS
class Message(BaseModel):
    user: UserInDB
    content: str = None
    edited: bool


class MessageInDB(Message):
    _id: ObjectId
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# CHATROOM MODELS
class Chatroom(BaseModel):
    chatroom_name: str
    members: Optional[List[UserInDB]] = []
    # messages: Optional[List[MessageInDB]] = []
    last_pinged: datetime = Field(default_factory=datetime.utcnow)
    active: bool = False


class ChatroomInDB(Chatroom):
    _id: ObjectId
    chatroom_name: str
    members: Optional[List[UserInDB]] = []
    date_created: datetime = Field(default_factory=datetime.utcnow)


# USER/AUTH MODELS
# class UserOutWithPassword(UserOut):
#     hashed_password: str

# class UserPasswordDB(UserIn):
#     id: PydanticObjectId

# class UserForm(BaseModel):
#     username: str
#     password: str

# class UserToken(Token):
#     account: UserOut

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: Optional[str] = None


# MISC MODELS
# class HttpError(BaseModel):
#     detail: str

# class PydanticObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, value: ObjectId | str) -> ObjectId:
#         if value:
#             try:
#                 ObjectId(value)
#             except ValueError:
#                 raise ValueError(f"Not a valid object id: {value}")
#         return value
