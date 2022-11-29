from pydantic import BaseModel
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


class UserOutWithPassword(UserOut):
    hashed_password: str


class UserQueries(Queries):
    DB_NAME = "user"
    COLLECTION = "users"

    def create(self, info=UserIn, response_model=UserOut):
        props = info.dict()

        self.collection.insert_one(props)

        props["id"] = str(props["_id"])
        return UserOut(**props)

    def get_all_users(self):
        users = []
        props = self.collection.find({})
        for document in props:
            document["id"] = str(document["_id"])
            users.append(UserOut(**document))
        return users

    def get_user(self, id):
        user = self.collection.find_one({"_id": id})
        user["id"] = str(user["_id"])
        return user

    def delete_user(self, id):
        self.collection.delete_one({"_id": id})
