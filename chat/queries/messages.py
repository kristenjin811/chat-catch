from pydantic import BaseModel
from fastapi import Response
from queries.client import Queries
from datetime import datetime


class MessageIn(BaseModel):
    message: str
    edited: bool
    # created: datetime.now

class MessageOut(BaseModel):
    id: str
    message: str
    edited: bool
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

    def create_or_update_message(self, id, info= MessageIn):
        message = self.collection.find_one({"_id": id})
        print("first::::", message)
        message["yellow"] = str(message["_id"])
        print("middle::::", message)
        self.collection.update_one({"_id": id}, {"$set": message})
        print("after::::", message)
