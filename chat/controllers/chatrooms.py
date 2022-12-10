from .users import get_user_db
from models import ChatroomInDB

# from pydantic import BaseModel, EmailStr
# from fastapi import Response
# from models import PydanticObjectId, UserIn, UserOut
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db
from utils import format_ids
import logging
from bson import ObjectId
import json

logger = logging.getLogger(__name__)

# jmoussa has set_room_activity, not sure what its purpose is

# controllers are functions that deal with the database

# async def create_chatroom()
#     client = await get_nosql_db()
#     db = client[MONGODB_DB_NAME]

# update chatroom by appending new message
# to messages list in chatroom document.


async def upload_message_to_chatroom(data):
    message_data = json.loads(data)
    print("message_data shape", message_data)
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    try:
        chatroom = await get_chatroom(message_data["chatroom_name"])
        # user = await get_user_db(message_data["user"]["username"])
        # message_data["user"] = user
        message_data.pop("chatroom_name", None)
        chatroom_name = message_data["chatroom_name"]
        chatroom = await get_chatroom(chatroom_name)
        message_body = {
            "user_name": message_data["user_name"],
            "content": message_data["content"],
        }
        collection = db.chatrooms
        print("collection", collection)
        collection.update_one(
            {"_id": ObjectId(chatroom["_id"])},
            {"$push": {"messages": message_body}},
        )
        return True
    except Exception as e:
        logger.error(f"error adding message to DB: {type(e)}{e}")
        return False


# insert created chatroom document into the
# chatrooms collection in mongodb database
async def insert_chatroom(username, chatroom_name, collection):
    chatroom = {}
    chatroom["chatroom_name"] = chatroom_name
    user = await get_user_db(username)
    chatroom["members"] = [user] if user is not None else []
    dbchatroom = ChatroomInDB(**chatroom)
    response = collection.insert_one(dbchatroom.dict())
    res = collection.find_one({"_id": response.inserted_id})
    res["_id"] = str(res["_id"])
    return res


# get all chatroom documents in chatrooms
# collection or subset defined as filter_list.
async def get_chatrooms():
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
    rows = collection.find()
    row_list = []
    for row in rows:
        f_row = format_ids(row)
        row_list.append(f_row)
    return row_list


# get one chatroom document from chatrooms
# collection specified by name add -> ChatRoomInDB
async def get_chatroom(chatroom_name) -> ChatroomInDB:
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
    row = collection.find_one({"chatroom_name": chatroom_name})
    if row is not None:
        row = format_ids(row)
        return row
    else:
        return None


# update chatroom document in chatrooms collection by
# adding username of user document to chatroom
# documents list of members
# async def add_user_to_chatroom(username: str, chatroom_name: str):
#     client = await get_nosql_db()
#     db = client[MONGODB_DB_NAME]
#     try:
#         chatroom = await get_chatroom(chatroom_name)
#         user = await get_user_db(username)
#         collection = db.chatrooms
#         username_list = [m["username"] for m in chatroom["members"]]
#         if user["username"] not in username_list:
#             logger.info(f"adding{user['username']} to members")
#             collection.update_one(
#                 {"_id": ObjectId(chatroom["_id"])},
#                 {"$push": {"members": user}},
#             )
#             return True
#         else:
#             logger.info(f"{user['username']} is already a member")
#             return True
#     except Exception as e:
#         logger.error(f"Error updating members:{e}")
#         return None


# update chatroom document in chatrooms collection by removing username of
# user document from chatroom documents list of members
# async def remove_user_from_chatroom(
#     user: User, chatroom_name: str, username=None
# ):
#     client = await get_nosql_db()
#     db = client[MONGODB_DB_NAME]
#     try:
#         chatroom = await get_chatroom(chatroom_name)
#         if username is not None and user is None:
#             user = await get_user_db(username)
#         collection = db.chatrooms
#         username_list = [m["username"] for m in chatroom["members"]]
#         if user["username"] in username_list:
#             logger.info(
#                 f"Removing{user['username']} from {chatroom_name} members"
#             )  # noqa
#             collection.update_one(
#                 {"_id": ObjectId(chatroom["_id"])},
#                 {"$pull": {"members": {"username": user["username"]}}},
#             )
#             return True
#         else:
#             logger.info(f"{user['username']} is already out of the chatroom")
#             return True
#     except Exception as e:
#         logger.error(f"Error updating members:{e}")
#         return False


async def delete_chatroom(chatroom_name: str):
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
    collection.delete_one({"chatroom_name": chatroom_name})


# async def add_message(message:str, collection):
#     client = await get_nosql_db()
#     db = client[MONGODB_DB_NAME]
#     collection = db.messages
#     collection.insert_one({"message": message})


async def add_message(message: str, collection):
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    collection = db.messages
    collection.insert_one({"message": message})


async def get_messages():
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    messages_collection = db.messages
    rows = messages_collection.find()
    row_list = []
    for row in rows:
        f_row = format_ids(row)
        row_list.append(f_row)
    return row_list
