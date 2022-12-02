from .users import get_user_db
from models import ChatroomInDB
# from pydantic import BaseModel, EmailStr
# from fastapi import Response
# from models import PydanticObjectId, UserIn, UserOut
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db
from utils import format_ids

# jmoussa has set_room_activity, not sure what its purpose is

# controllers are functions that deal with the database

# async def create_chatroom()
#     client = await get_nosql_db()
#     db = client[MONGODB_DB_NAME]

# update chatroom by appending new message
# to messages list in chatroom document.


async def upload_message_to_chatroom(data):
    pass


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
async def add_user_to_chatroom(username: str, chatroom_name: str):
    pass


# update chatroom document in chatrooms collection by removing username of
# user document from chatroom documents list of members
async def remove_user_from_chatroom(username: str, chatroom_name: str):
    pass


async def delete_chatroom(chatroom_name: str):
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
    collection.delete_one({"chatroom_name": chatroom_name})
