from pydantic import BaseModel
from typing import Optional
# import pymongo
# import os
from pymongo.errors import DuplicateKeyError
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db
from pymongo import MongoClient
from fastapi import (
    Depends,
)


class Account(BaseModel):
    id: str
    email: str
    hashed_password: str


class AccountIn(BaseModel):
    email: str
    password: str


class AccountOut(BaseModel):
    id: str
    email: str


class DuplicateAccountError(ValueError):
    pass


class AccountRepository:
    async def get_one(self, email: str) -> Optional[Account]:
        client = await get_nosql_db()
        db = client[MONGODB_DB_NAME]

        print("db ACCOUNT QUERIES.PY :::::::::", db)

        result = db.accounts.find_one({"email": email})
        if result:
            result["id"] = str(result["_id"])
        return Account(**result)

    async def create(self, account: AccountIn, hashed_password: str) -> Account:
        print("This is queries create   :::::::::::::")
        client: MongoClient = Depends(get_nosql_db)
        print("client ACCOUNT QUERIES.PY:::::::::::::::", client)

        db = await client[MONGODB_DB_NAME]

        print("db ACCOUNT QUERIES.PY::::::::::::::::", db)

        props = account.dict()

        props["hashed_password"] = hashed_password

        props.pop("password")
        try:

            db.accounts.insert_one(props)
        except DuplicateKeyError:
            raise DuplicateAccountError()
        props["id"] = str(props["_id"])
        return Account(**props)
