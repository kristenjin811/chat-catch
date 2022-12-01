from fastapi import (
    APIRouter,
    # Depends,
    # Response,
    # Request,
    # status,
    # HTTPException,
)

# from models import ChatroomIn, ChatroomOut
# from jwtdown_fastapi.authentication import Token
# import pymongo
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
@router.post("/chatrooms", tags=["Rooms"])
async def create_chatroom(
    # request: ChatRoomCreateRequest,
    # client: MongoClient = Depends(get_nosql_db),
    # current_user: User = Depends(get_current_active_user),
):
    # db = client[MONGODB_DB_NAME]
    # collection = db.chatrooms
    # response = await insert_chatroom(
    #     request.username, request.chatroom_name, collection
    # )
    # return response
    pass
