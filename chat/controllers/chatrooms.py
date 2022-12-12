from .users import get_user_db
from models import ChatroomInDB
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db
from utils import format_ids
import logging
from bson import ObjectId
import json

logger = logging.getLogger(__name__)


async def upload_message_to_chatroom(data):
    message_data = json.loads(data)
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    try:
        current_user = message_data["user_name"]
        chatroom_name = message_data["chatroom_name"]
        chatroom = await get_chatroom(chatroom_name)
        message_body = {
            "user_name": message_data["user_name"],
            "content": message_data["content"],
        }
        if current_user not in chatroom["members"]:
            await upload_member_to_chatroom(current_user, chatroom_name)
        collection = db.chatrooms
        collection.update_one(
            {"_id": ObjectId(chatroom["_id"])},
            {"$push": {"messages": message_body}},
        )
        return True
    except Exception as e:
        logger.error(f"error adding message to DB: {type(e)}{e}")
        return False


async def upload_member_to_chatroom(current_user, chatroom_name):
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    try:
        new_member = current_user
        chatroom = await get_chatroom(chatroom_name)
        collection = db.chatrooms
        collection.update_one(
            {"_id": ObjectId(chatroom["_id"])},
            {"$push": {"members": new_member}},
        )
        return True
    except Exception as e:
        logger.error(
            f"error adding the user to members_list in DB: {type(e)}{e}"
        )
        return False


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


async def delete_chatroom(chatroom_name: str):
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
    collection.delete_one({"chatroom_name": chatroom_name})
