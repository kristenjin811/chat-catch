from pydantic import BaseModel
from fastapi import Response
from queries.client import Queries
from datetime import datetime


class MessageIn(BaseModel):
    message: str
    edited: bool


class MessageOut(BaseModel):
    message: str
    edited: bool


class UserQueries(Queries):
    DB_NAME = "user"
    COLLECTION = "users"

    def create(self, info = UserIn, response_model = UserOut):
    # created: datetime.now




class MessageQueries(Queries):
    DB_NAME = "message"
    COLLECTION = "messages"

    def create(self, info = MessageIn, response_model = MessageOut):
        props = info.dict()

        try:
            self.collection.insert_one(props)
        except:
            pass
        props["id"] = str(props["_id"])
        return UserOut(**props)

    def get_all_users(self):
        users = []
        props = self.collection.find({})
        for document in props:
            document["id"] = str(document["_id"])
            users.append(UserOut(**document))
        return users




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
