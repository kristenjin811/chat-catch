from fastapi import (
    FastAPI,
    # WebSocket,
    # WebSocketDisconnect
)
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

# from api.users import get_user
# from controllers.users import get_user_db
from mongodb import connect_to_mongo, close_mongo_connection, get_nosql_db
from config import MONGODB_DB_NAME
import pymongo
import logging
from websocket_manager import ConnectionManager

# import json
# from starlette.websockets import WebSocketState
from api import router as api_router

# from authenticator import authenticator


app = FastAPI()
logger = logging.getLogger(__name__)
# app.include_router(users.router)
# app.include_router(authenticator.router)
# app.include_router(messages.router)
# app.include_router(auth.auth.router)
# app.include_router(websocket.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    try:
        db.create_collection("users")
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
    try:
        db.create_collection("chatrooms")
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
    try:
        db.create_collection("messages")
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)
    try:
        user_collection = db.users
        chatroom_collection = db.chatrooms
        user_collection.create_index(
            "username",
            name="username",
            unique=True,
        )
        chatroom_collection.create_index(
            "chatroom_name",
            name="chatroom_name",
            unique=True,
        )
    except pymongo.errors.CollectionInvalid as e:
        logging.warning(e)


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


# @app.get("/api/launch-details")
# def launch_details():
#     return {
#         "launch_details": {
#             "year": 2022,
#             "month": 12,
#             "day": "9",
#             "hour": 19,
#             "min": 0,
#             "tz:": "PST",
#         }
#     }

manager = ConnectionManager


@app.get("/")
def homepage():
    with open("index.html") as f:
        return HTMLResponse(f.read())


# @app.websocket("/ws/{room_name}/{user_name}")
# async def websocket_endpoint(websocket: WebSocket, room_name, user_name):
#     try:
#         # add user
#         await manager.connect(websocket, room_name)
#         await add_user_to_room(user_name, room_name)
#         room = await get_room(room_name)
#         data = {
#             "content": f"{user_name} has entered the chat",
#             "user": {"username": user_name},
#             "room_name": room_name,
#             "type": "entrance",
#             "new_room_obj": room,
#         }
#         await manager.broadcast(f"{json.dumps(data, default=str)}")
#         # wait for messages
#         while True:
#             if websocket.application_state == WebSocketState.CONNECTED:
#                 data = await websocket.receive_text()
#                 message_data = json.loads(data)
#                 if (
#                     "type" in message_data
#                     and message_data["type"] == "dismissal"
#                 ):
#                     logger.warning(message_data["content"])
#                     logger.info("Disconnecting from Websocket")
#                     await manager.disconnect(websocket, room_name)
#                     break
#                 else:
#                     await upload_message_to_room(data)
#                     logger.info(f"DATA RECEIVED: {data}")
#                     await manager.broadcast(f"{data}")
#             else:
#                 logger.warning(
#                     f"Websocket state: {websocket.application_state},
#  reconnecting..."
#                 )
#                 await manager.connect(websocket, room_name)
#     except Exception as ex:
#         template = "An exception of type {0} occured, Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         logger.error(message)
#         # remove user
#         logger.warning("Disconnecting Websocket")
#         await remove_user_from_room(None, room_name, username=user_name)
#         room = await get_room(room_name)
#         data = {
#             "content": f"{user_name} has left the chat",
#             "user": {"username": user_name},
#             "room_name": room_name,
#             "type": "dismissal",
#             "new_room_obj": room,
#         }
#         await manager.broadcast(f"{json.dumps(data, default=str)}")
#         await manager.disconnect(websocket, room_name)


app.include_router(api_router, prefix="/api")
