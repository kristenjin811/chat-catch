# this models.py file holds all the models
from fastapi import Response
from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from models import PydanticObjectId
from datetime import datetime


class User(BaseModel):
    username: str
    hashed_password: str
    salt: str
    avatar: Optional[str]


class UserIn(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str


class UserOut(BaseModel):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str


class UserOutWithPassword(UserOut):
    hashed_password: str


class UserPasswordDB(UserIn):
    id: PydanticObjectId


class UserForm(BaseModel):
    username: str
    password: str


class UserInDB(User):
    _id: ObjectId
    date_created: datetime = Field(default=datetime.utcnow)


# class UserToken(Token):
#     account: UserOut


class HttpError(BaseModel):
    detail: str


class MessageIn(BaseModel):
    message: str
    edited: bool


class MessageOut(BaseModel):
    message: str
    edited: bool


class MessagesIn(BaseModel):
    message: str
    from_time: str


class MessagesQueries:
    def get_all_messages(self):
        result = list(db.messages.find())
        for message in result:
            message["id"] = message["_id"]
        return result


class MessageQueries(Queries):
    DB_NAME = "message"
    COLLECTION = "messages"

    def create(self, info=MessageIn, response_model=MessageOut):
        props = info.dict()

        try:
            self.collection.insert_one(props)
        except:
            pass
        props["id"] = str(props["_id"])
        return MessageOut(**props)

    def get_all_messages(self):
        messages = []
        props = self.collection.find({})
        for document in props:
            document["id"] = str(document["_id"])
            messages.append(MessageOut(**document))
        return messages

    def get_message(self, id):
        message = self.collection.find_one({"_id": id})
        message["id"] = str(message["_id"])
        return message

    def delete_message(self, id):
        self.collection.delete_one({"_id": id})


class Message(BaseModel):
    user: UserInDB
    content: str = None


class MessageInDB(Message):
    _id: ObjectId
    timestamp: datetime = Field(default=datetime.utcnow)


class ChatroomIn(BaseModel):
    name: str
    owner: str
    members: str
    messages: str


class ChatroomOut(BaseModel):
    id: str
    name: str


class ChatroomQueries(Queries):
    DB_NAME = "chatroom"
    COLLECTION = "chatrooms"

    def create(self, info=ChatroomIn, response_model=ChatroomOut):
        props = info.dict()
        try:
            self.collection.insert_one(props)
        except:
            pass
        props["id"] = str(props["_id"])
        return ChatroomOut(**props)

    def get_all(self, info=ChatroomIn, response_model=ChatroomOut):
        props = info.dict()
        try:
            self.collection.insert_one(props)
        except:
            pass
        props["id"] = str(props["_id"])
        return ChatroomOut(**props)


class Room(BaseModel):
    room_name: str
    members: Optional[List[UserInDB]] = []
    messages: Optional[List[MessageInDB]] = []
    last_pinged: datetime = Field(default=datetime.utcnow)
    active: bool = False


class RoomInDB(Room):
    _id: ObjectId
    date_created: datetime = Field(default=datetime.utcnow)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


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
