from typing import List, Optional

from pydantic import BaseModel, Field
from dateime import datetime
from uuid import UUID, uuid4


class User(BaseModel):
    username: str
    hashed_password: str
    salt: str


class UserInDB(User):
    _id: UUID = Field(default=uuid4)
    date_created: datetime = Field(default=datetime.utcnow)


class Message(BaseModel):
    user: UserInDB
    content: str = None


class MessageInDB(Message):
    _id: UUID = Field(default=uuid4)
    timestamp: datetime = Field(default=datetime.utcnow)


class Room(BaseModel):
    room_name: str
    members: Optional[List[UserInDB]] = None
    messages: Optional[List[MessageInDB]] = None
    last_pinged: datetime = Field(default=datetime.utcnow)


class RoomInDB(Room):
    _id: UUID = Field(default=uuid4)
    date_created: datetime = Field(default=datetime.utcnow)
