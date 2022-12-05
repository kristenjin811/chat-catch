from pydantic import BaseModel

# from typing import Optional


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
