from pydantic import BaseModel


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class ChatroomCreateRequest(BaseModel):
    username: str
    chatroom_name: str


class AddMessageRequest(BaseModel):
    username: str
    message: str
    chatroom: str


class ChatroomMessageRequest(BaseModel):
    username: str
    chatroom_name: str
    message: str
