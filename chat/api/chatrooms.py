from fastapi import (
    APIRouter,
    Depends,
)
from controllers.chatrooms import (
    insert_chatroom,
    get_chatrooms,
    get_chatroom,
    delete_chatroom,
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
):
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
    res = await insert_chatroom(
        request.username, request.chatroom_name, collection
    )
    return res


@router.put("/chatrooms/{chatroom_name}")
async def add_message(
    request: AddMessageRequest,
    client: MongoClient = Depends(get_nosql_db),
):
    db = client[MONGODB_DB_NAME]
    collection = db.chatrooms
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
    client: MongoClient = Depends(get_nosql_db),
):
    chatrooms = await get_chatrooms()
    return chatrooms


@router.get("/chatrooms/{chatroom_name}")
async def get_single_room(
    chatroom_name
):
    chatroom = await get_chatroom(chatroom_name)
    formatted_chatroom = format_ids(chatroom)
    return formatted_chatroom


@router.delete("/chatrooms/{chatroom_name}")
async def delete_chatroom_db(chatroom_name: str):
    try:
        await delete_chatroom(chatroom_name)
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
