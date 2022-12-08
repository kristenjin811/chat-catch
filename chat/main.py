from fastapi import (
    FastAPI,
    WebSocket,
    # WebSocketDisconnect
)
from starlette.websockets import WebSocketState
from websocket_manager import ConnectionManager
from controllers.chatrooms import (
    get_chatroom,
    remove_user_from_chatroom,
    add_user_to_chatroom,
    upload_message_to_chatroom,
)
from mongodb import connect_to_mongo, close_mongo_connection, get_nosql_db
from config import MONGODB_DB_NAME
import pymongo
import logging
import json
from api import router as api_router

# # from authenticator import authenticator
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()
app.include_router(api_router, prefix="/api")
logger = logging.getLogger(__name__)
# app.include_router(users.router)
# app.include_router(authenticator.router)
# app.include_router(messages.router)
# app.include_router(auth.auth.router)
# app.include_router(websocket.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # [os.environ.get("CORS_HOST", "http://localhost:3000")],
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


manager = ConnectionManager()


# @app.get("/")
# def homepage():
#     with open("index.html") as f:
#         return HTMLResponse(f.read())


@app.websocket("/ws/{chatroom_name}/{user_name}")
async def websocket_endpoint(websocket: WebSocket, chatroom_name, user_name):
    try:
        # add user
        await manager.connect(websocket)
        # await add_user_to_chatroom(user_name, chatroom_name)
        chatroom = await get_chatroom(chatroom_name)
        data = json.dumps(
            {
                "content": f"{user_name} has entered the chat",
                "user_name": user_name,
                "chatroom_name": chatroom_name,
                "type": "entrance",
                "new_chatroom_obj": chatroom,
            },
            default=str,
        )
        await manager.broadcast(data)
        # wait for messages
        while True:
            if websocket.application_state == WebSocketState.CONNECTED:
                data = await websocket.receive_text()
                print("---Receiving Text")
                message_data = json.loads(data)
                if (
                    "type" in message_data
                    and message_data["type"] == "dismissal"
                ):
                    logger.warning(message_data["content"])
                    logger.info("Disconnecting from Websocket")
                    await manager.disconnect(websocket)
                    break
                else:
                    print("---Attempting to Upload Message To Chatroom")
                    await upload_message_to_chatroom(data)
                    print("---Successful Upload!")
                    logger.info(f"DATA RECEIVED: {data}")
                    await manager.broadcast(f"{data}")
            else:
                logger.warning(
                    f"Websocket state:{websocket.application_state},reconnecting..."
                )  # noqa
                await manager.connect(websocket)
    except Exception as e:
        template = "An exception of type {0} occurred, Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        logger.error(message)
        # remove user
        logger.warning("Disconnecting Websocket")
        # await remove_user_from_chatroom(
        #   None, chatroom_name,
        #   username=user_name
        #   )
        chatroom = await get_chatroom(chatroom_name)
        data = json.dumps(
            {
                "content": f"{user_name} has left the chat",
                "user_name": user_name,
                "chatroom_name": chatroom_name,
                "type": "dismissal",
                "new_chatroom_obj": chatroom,
            },
            default=str,
        )
        await manager.broadcast(data)
        await manager.disconnect(websocket)
