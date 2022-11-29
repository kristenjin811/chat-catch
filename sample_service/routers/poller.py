import sys
import time
import json
import requests
import os
import pymongo
from bson.json_util import dumps
from fastapi import APIRouter, Depends, Response
from queries.poller import PollerQueries, PollerIn, PollerOut
from fastapi import APIRouter, Depends, Response, Request
from queries.users import UserQueries
from bson.objectid import ObjectId
router = APIRouter()

MONGO_URL = os.environ.get("DATABASE_URL")
client = pymongo.MongoClient(MONGO_URL)


# db = client.user
# coll = db.users
# cursor = coll.find()
# print(db.users.find())



@router.get("/api/users")
def get_users_to_poller(
    response: Response, users: UserQueries = Depends()
):
    response = users.get_all_users()
    return response






@router.post("/api/chat/userVO", response_model = PollerOut)
async def create_account(
    info: PollerIn,  # this is what should be in the body
    users: PollerQueries = Depends(),

):

    try:
       info = users.create(info)

    except:
        pass
    print("USER IN::::::", PollerIn)
    print("USER OUT::::::", PollerOut)

    return info

@router.get("/api/chat/userVO")
def get_polled_users(
    response: Response, users: PollerQueries = Depends()
):
    response = users.get_all_users()
    return response

@router.get("/api/chat/userVO/{id}", response_model = PollerOut)
def get_user(
    id: str,
    user: Response, users: PollerQueries = Depends()
):
    user = users.get_user(ObjectId(id))
    return PollerOut(**user)

@router.delete("/api/chat/userVO/{id}", response_model=bool)
async def delete_user(
    id: str,
    user: Response, users: PollerQueries = Depends()
) -> bool:
    users.delete_user(ObjectId(id))
    return True









def getting_users_to_puller():
        response = requests.get(get_users_to_poller)
        content = json.loads(response.content)
        users = []



        for user in content:
                if user in users:
                        print(user)
#                 else:
#                         users.append(user)
#                         add_users()

# def add_users():
#     print("added")

def poll():
    while True:
        print('Checking for any new users...')
        try:
            getting_users_to_puller()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(10)

if __name__ == "__main__":
    poll()
