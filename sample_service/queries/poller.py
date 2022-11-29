from pydantic import BaseModel
from fastapi import Response
from queries.client import Queries


class PollerIn(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str


class PollerOut(BaseModel):
    id: str
    username: str
    email: str
    first_name: str
    last_name: str

class UserOutWithPassword(PollerOut):
    hashed_password: str



class PollerQueries(Queries):
    DB_NAME = "chat"
    COLLECTION = "userVO"

    def create(self, info = PollerIn, response_model = PollerOut):
        props = info.dict()

        try:
            self.collection.insert_one(props)
        except:
            pass
        props["id"] = str(props["_id"])
        return PollerOut(**props)

    def get_all_users(self):
        users = []
        props = self.collection.find({})
        for document in props:
            document["id"] = str(document["_id"])
            users.append(PollerOut(**document))
        return users

    def get_user(self, id):
        user = self.collection.find_one({"_id": id})
        user["id"] = str(user["_id"])
        return user

    def delete_user(self, id):
        self.collection.delete_one({"_id": id})

    
