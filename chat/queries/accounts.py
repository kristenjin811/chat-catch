from pydantic import BaseModel

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


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class AccountQueries(Queries):
    DB_NAME = "accounts"
    COLLECTION = "accounts"


    def get(self, email: str):
        user = self.collection.find_one({"email": email})
        user["id"] = str(user["_id"])
        return AccountOutWithPassword(**user)

    def create(self, info: AccountIn, hashed_password: str):
        props = info.dict()
        props["hashed_password"] = hashed_password
        try:
            self.collection.insert_one(props)
        except Exception as e:
            print(e)
        props["id"] = str(props["_id"])
        return AccountOutWithPassword(**props)
