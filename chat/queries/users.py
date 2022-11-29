from pydantic import BaseModel, EmailStr
from fastapi import Response
from queries.client import Queries


class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    first_name: str
    last_name: str


class UserOutWithPassword(UserOut):
    hashed_password: str


class AccountPasswordDB(AccountIn):
    id: PydanticObjectId


class UserQueries(Queries):
    DB_NAME = "user"
    COLLECTION = "users"

    def create(self, info=UserIn, response_model=UserOut):
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

    def get_user(self, id):
        user = self.collection.find_one({"_id": id})
        user["id"] = str(user["_id"])
        return user

    def delete_user(self, id):
        self.collection.delete_one({"_id": id})

    # def create(self, info: UserIn, hashed_password: str) -> AccountPasswordDB:
    #     props = info.dict()
    #     props["password"] = hashed_password

    #     try:
    #         self.collection.insert_one(props)
    #     except DuplicateKeyError:
    #         raise DuplicateAccountError()
    #     props["id"] = str(props["_id"])
    #     return AccountPasswordDB(**props)
