from pydantic import BaseModel
from fastapi import Response
from queries.client import Queries


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
