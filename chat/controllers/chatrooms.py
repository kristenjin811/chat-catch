from pydantic import BaseModel, EmailStr
from fastapi import Response
from models import PydanticObjectId, UserIn, UserOut
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db


# jmoussa has set_room_activity, not sure what its purpose is

# controllers are functions that deal with the database

# async def create_chatroom()
#     client = await get_nosql_db()
#     db = client[MONGODB_DB_NAME]

# update chatroom by appending new message to messages list in chatroom document.
async def upload_message_to_chatroom(data):
    pass


# insert created chatroom document into the chatrooms collection in mongodb database
async def insert_chatroom(username, chatroom_name, collection):
    pass


# get all chatroom documents in chatrooms collection or subset defined as filter_list.
async def get_chatrooms(filter_list: list = None):
    pass


# get one chatroom document from chatrooms collection specified by name
async def get_chatroom(chatroom_name) -> ChatRoomInDB:
    pass


# update chatroom document in chatrooms collection by adding username of
# user document to chatroom documents list of members
async def add_user_to_chatroom(username: str, chatroom_name: str):
    pass


# update chatroom document in chatrooms collection by removing username of
# user document from chatroom documents list of members
async def remove_user_from_chatroom(username: str, chatroom_name: str):
    pass
