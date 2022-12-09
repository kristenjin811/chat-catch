from fastapi import FastAPI, WebSocket, WebSocketDisconnect
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
        # print("chatroom_name ---- 98 main", chatroom_name)
        await manager.connect(websocket, chatroom_name, user_name)
        # add user
        # await add_user_to_chatroom(user_name, chatroom_name)
        # print("chatroom_name ---- 102 main", chatroom_name)
        chatroom = await get_chatroom(chatroom_name)
        # print("chatroom_name --- 104 main", chatroom_name)
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
        # print("data ---- 115 main", data)
        await manager.broadcast(data, chatroom_name, user_name)
        # wait for messages
        # print("chatroom_name ---- 118 main", chatroom_name)
        while True:
            # print("main 120 --- top of forever loop")
            # print("chatroom_name ---- 121 main", chatroom_name)
            if websocket.application_state == WebSocketState.CONNECTED:

                # print("main 123 ---inside if")
                try:
                    data = await websocket.receive_text()
                except WebSocketDisconnect as e:
                    manager.disconnect(chatroom_name, user_name)
                    print("tried to receive_text and excepted....", e)
                # print("data ---- 125 main", data)
                message_data = json.loads(data)
                if (
                    "type" in message_data
                    and message_data["type"] == "dismissal"
                ):
                    logger.warning(message_data["content"])
                    logger.info("Disconnecting from Websocket")
                    await manager.disconnect(
                        chatroom_name,
                        user_name,
                    )
                    break
                else:
                    # print("chatroom_name ---- 139 main", chatroom_name)
                    # print("data in else before upload main", data)
                    await upload_message_to_chatroom(data)
                    logger.info(f"DATA RECEIVED: {data}")

                    await manager.broadcast(data, chatroom_name, user_name)
                    # print("main.py line 139 --- bottom of forever loop")
            else:
                print("main 142 ---inside else")
                logger.warning(
                    f"Websocket state:{websocket.application_state},reconnecting..."
                )  # noqa
                await manager.connect(websocket, chatroom_name, user_name)
                print("main 147 --- second attempt to connect")
    except Exception as e:
        # template = "An exception of type {0} occurred, Arguments:\n{1!r}"
        # message = template.format(type(e).__name__, e.args)
        # logger.error(message)
        # remove user
        # logger.warning("Disconnecting Websocket")
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
        print("we have been dismissed!")
        if websocket.application_state == WebSocketState.CONNECTED:
            await manager.broadcast(data, chatroom_name, user_name)
            await manager.disconnect(chatroom_name, user_name)
