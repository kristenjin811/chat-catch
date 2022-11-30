from pydantic import BaseModel
from queries.client import Queries


class MessageIn(BaseModel):
    message: str
    edited: bool


class MessageOut(BaseModel):
    id: str
    message: str
    edited: bool


class MessageQueries(Queries):
    DB_NAME = "message"
    COLLECTION = "messages"

    def create(self, info=MessageIn, response_model=MessageOut):
        props = info.dict()
        try:
            self.collection.insert_one(props)
        except Exception as e:
            print(e)
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
