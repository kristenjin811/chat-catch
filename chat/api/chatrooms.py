from fastapi import (
    APIRouter,
    Depends,
)
from controllers.chatrooms import (
    ChatroomQueries,
    upload_message_to_chatroom,
)
from utils import format_ids
import json
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db
from pymongo import MongoClient
from request_forms import (
    ChatroomCreateRequest,
    AddMessageRequest,
    ChatroomMessageRequest,
)

router = APIRouter()


@router.post("/chatrooms")
async def create_chatroom(
    request: ChatroomCreateRequest,
    client: MongoClient = Depends(get_nosql_db),
    Chatrooms: ChatroomQueries = Depends(),
):
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
    res = await Chatrooms.insert_chatroom(
        request.username, request.chatroom_name, collection
    )
    return res


@router.put("/chatrooms/{chatroom_name}")
async def add_message(
    request: AddMessageRequest,
    client: MongoClient = Depends(get_nosql_db),
    Chatrooms: ChatroomQueries = Depends(),
):
    chatroom = await get_chatroom(request.chatroom)
    collection.update_one(
        {"chatroom_name": chatroom["chatroom_name"]},
        {
            "$push": {
                "messages": {
                    "username": request.username,
                    "content": request.message,
                }
            }
        },
    )
    return True


@router.get("/chatrooms")
async def get_all_chatrooms(
    Chatrooms: ChatroomQueries = Depends(),
):
    chatrooms = await Chatrooms.get_chatrooms()
    return chatrooms


@router.get("/chatrooms/{chatroom_name}")
async def get_single_room(
    chatroom_name
    Chatrooms: ChatroomQueries = Depends(),
):
    chatroom = await Chatrooms.get_chatroom(chatroom_name)
    formatted_chatroom = format_ids(chatroom)
    return formatted_chatroom


@router.delete("/chatrooms/{chatroom_name}")
async def delete_chatroom_db(
    Chatrooms: ChatroomQueries = Depends(),
    chatroom_name: str
    ):
    try:
        await Chatrooms.delete_chatroom(chatroom_name)
    except Exception as e:
        return e
    return True


@router.put("/chatrooms/{chatroom_name}")
async def create_message(
    request: ChatroomMessageRequest,
):
    data = {
        "username": request.username,
        "chatroom_name": request.chatroom_name,
        "content": request.message,
    }
    res = await upload_message_to_chatroom(f"{json.dumps(data, default=str)}")
    return res
