# from fastapi import Response
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from datetime import datetime

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
    message: Message
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# CHATROOM MODELS
class Chatroom(BaseModel):
    chatroom_name: str
    members: Optional[List[UserInDB]] = []
    messages: Optional[List[MessageInDB]] = []
    last_pinged: datetime = Field(default_factory=datetime.utcnow)
    active: bool = False


class ChatroomInDB(Chatroom):
    _id: ObjectId
    chatroom_name: str
    members: Optional[List[UserInDB]] = []
    date_created: datetime = Field(default_factory=datetime.utcnow)
