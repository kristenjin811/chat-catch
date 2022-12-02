# import json
# import os
# import sys
# import time

# import pymongo
# import requests

# # from bson.json_util import dumps
# # from bson.objectid import ObjectId
# from fastapi import (
#     APIRouter,
#     # Depends,
#     # Response
# )

# # from queries.poller import PollerIn, PollerOut, PollerQueries
# # from queries.users import UserQueries

# router = APIRouter()


# MONGO_URL = os.environ.get("DATABASE_URL")
# client = pymongo.MongoClient(MONGO_URL)


# @router.get("/api/chat/userVO")
# def getting_users_to_puller():
#     response = requests.get("http://localhost:8000/api/users")
#     content = json.loads(response.content)
#     users = []
#     for user in content:
#         if user in users:
#             continue
#         else:
#             users.append(user)
#             requests.post("http://localhost:8081/db/chat/userVO")


# def poll():
#     while True:
#         print("Checking for any new users...")
#         try:
#             getting_users_to_puller()
#         except Exception as e:
#             print(e, file=sys.stderr)
#         time.sleep(10)


# if __name__ == "__main__":
#     poll()
