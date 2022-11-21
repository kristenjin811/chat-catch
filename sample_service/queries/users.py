from pydantic import BaseModel
from fastapi import Response
from queries.client import Queries

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


class UserQueries(Queries):
    DB_NAME = "user"
    COLLECTION = "users"

    def create(self, info = UserIn, response_model = UserOut):
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
