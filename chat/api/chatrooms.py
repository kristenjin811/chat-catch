from fastapi import (
    APIRouter,
    Depends,
    # Response,
    # Request,
    # status,
    # HTTPException,
)
from controllers.chatrooms import (
    insert_chatroom,
    get_chatrooms,
    get_chatroom,
    delete_chatroom,
    upload_message_to_chatroom
)
from utils import format_ids

# from controllers.users import get_user_db
from config import MONGODB_DB_NAME
from mongodb import get_nosql_db
from pymongo import MongoClient
from request_forms import ChatroomCreateRequest, AddMessageRequest
from request_forms import ChatroomCreateRequest,ChatroomMessageRequest

# from models import ChatroomIn, ChatroomOut
# from jwtdown_fastapi.authentication import Token

# from pydantic import BaseModel

router = APIRouter()

# jmoussa has create_room, add_user_to_room_members,
# get_all_rooms, get_single_room

# endpoints:
# create_chatroom <@router.post("/api/chatrooms")>
# get_all_chatrooms <@router.get("/api/chatrooms")>
# get_chatroom <@router.get("/api/chatrooms/{chatroom_id}")>
# delete_chatroom <@router.delete("/api/chatrooms/{chatroom_id}">
# add_user_to_chatroom_members <@router.put("/api/chatrooms/{chatroom_id}")>


# post request to localhost:8000/api/chatroom
# (do not understand tags...) browser is presented
# with request form for input, function gets current
# user and mongoclient. Then uses the controller
# function insert_chatroom to add created chatroom to the database
@router.post("/chatrooms")
async def create_chatroom(
    request: ChatroomCreateRequest,
    client: MongoClient = Depends(get_nosql_db),
    # current_user: User = Depends(get_current_active_user),
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
    # current_user: User = Depends(get_current_active_user),
):
    chatrooms = await get_chatrooms()
    return chatrooms


@router.get("/chatrooms/{chatroom_name}")
async def get_single_room(
    chatroom_name,
    # current_user: User = Depends(get_current_active_user),
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


# @router.post("/chatrooms")
# async def create_chatroom(
#     request: ChatroomCreateRequest,
#     client: MongoClient = Depends(get_nosql_db),
#     # current_user: User = Depends(get_current_active_user),
# ):
#     db = client[MONGODB_DB_NAME]
#     collection = db.messages
#     res = await insert_chatroom(
#         request.message, collection
#     )
#     return res
@router.post("/chatrooms")
async def create_chatroom(
    request: ChatroomCreateRequest,
    client: MongoClient = Depends(get_nosql_db),
    # current_user: User = Depends(get_current_active_user),
):
    db = client[MONGODB_DB_NAME]
    collection = db.messages
    res = await insert_chatroom(
        request.message, collection
    )
    return res

@router.post("/chatrooms")
async def create_message(
    request: ChatroomMessageRequest,
    client: MongoClient = Depends(get_nosql_db),
):
    db = client[MONGODB_DB_NAME]
    collection = db.messages
    res = await upload_message_to_chatroom(
        request.message, collection
    )
    return res
