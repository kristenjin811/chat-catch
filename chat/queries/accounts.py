from pydantic import BaseModel
from typing import Optional
import os
from pymongo.errors import DuplicateKeyError
from queries.client import Queries





class DuplicateAccountError(ValueError):
    pass


class AccountIn(BaseModel):
    email: str
    password: str
    full_name: str

class AccountOut(BaseModel):
    id: str
    email: str
    full_name: str


class AccountOutWithPassword(BaseModel):
    hashed_password: str





class AccountQueries(Queries):
    DB_NAME = "accounts"
    COLLECTION = "accounts"


    def get(self, email: str):


        # print("db ACCOUNT QUERIES.PY :::::::::", db)


        user = self.collection.find_one({"email": email})
        user["id"] = str(user["id"])
        return AccountOutWithPassword(**user)
        # if result:
        #     result["id"] = str(result["_id"])
        # return Account(**result)

    def create(self, info: AccountIn, hashed_password: str):
        # -> Account
        print("This is queries create   ::::::::::::::::::::::::::")

        # print("client ACCOUNT QUERIES.PY:::::::::::::::::::::::::::::::::::", client)




        # print("db ACCOUNT QUERIES.PY::::::::::::::::",db)

        props = info.dict()

        props["hashed_password"] = hashed_password

        props.pop("password")
        try:

            self.collection.insert_one(props)
        except DuplicateKeyError:
            raise DuplicateAccountError()
        props["id"] = str(props["_id"])
        return AccountOutWithPassword(**props)
