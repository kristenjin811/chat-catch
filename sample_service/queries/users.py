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


class UserQueries(Queries):
    DB_NAME = "user"
    COLLECTION = "users"

    def create(self, info: UserIn):
        props = info.dict()

        try:
            self.collection.insert_one(props)
        except:
            pass
