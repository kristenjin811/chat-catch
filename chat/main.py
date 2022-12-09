from typing import Union

from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    websockets,
    status,
)
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <label>Item ID: <input type="text" id="itemId" autocomplete="off" value="foo"/></label>
            <label>Chatroom: <input type="text" id="chatroom" autocomplete="off" value="some-key-chatroom"/></label>
            <button onclick="connect(event)">Connect</button>
            <hr>
            <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
        var ws = null;
            function connect(event) {
                var itemId = document.getElementById("itemId")
                var chatroom = document.getElementById("chatroom")
                ws = new WebSocket("ws://localhost:8000/items/" + itemId.value + "/ws?chatroom=" + chatroom.value);
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                event.preventDefault()
            }
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


async def get_cookie_or_chatroom(
    websocket: WebSocket,
    session: Union[str, None] = Cookie(default=None),
    chatroom: Union[str, None] = Query(default=None),
):
    if session is None and chatroom is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return session or chatroom


@app.websocket("/items/{item_id}/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    item_id: str,
    q: Union[int, None] = None,
    cookie_or_chatroom: str = Depends(get_cookie_or_chatroom),
):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(
            f"Session cookie or query chatroom value is: {cookie_or_chatroom}"
        )
        if q is not None:
            await websocket.send_text(f"Query parameter q is: {q}")
        await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")

from fastapi import (
    FastAPI,
    WebSocket,
    # WebSocketDisconnect
)
from starlette.websockets import WebSocketState
from websocket_manager import ConnectionManager
from controllers.chatrooms import (
    get_chatroom,
    # remove_user_from_chatroom,
    # add_user_to_chatroom,
    upload_message_to_chatroom,
)
from mongodb import connect_to_mongo, close_mongo_connection, get_nosql_db
from config import MONGODB_DB_NAME
import pymongo
import logging
import json
from api import router as api_router

# # from authenticator import authenticator
# from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()
app.include_router(api_router, prefix="/api")
logger = logging.getLogger(__name__)


app.add_middleware(
    CORSMiddleware,
    # allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_origins=["*"],
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

# STREAMLINED - THIS WORKS FOR SURE
@app.websocket("/ws/{chatroom_name}/{user_name}")
async def websocket_endpoint(
    websocket: WebSocket, chatroom_name: str, user_name: str
):
    try:
        await manager.connect(websocket)
        while True:
            print("line 97")
            if websocket.application_state == WebSocketState.CONNECTED:
                data = await websocket.receive_text()
                # message_data = json.loads(data)
                print("line 100", data)
                # print(f"PLZ WORK: {message_data}")
                await upload_message_to_chatroom(data)
                print("line 104")
                logger.info(f"DATA RECEIVED: {data}")
                await manager.broadcast(f"{data}")
            else:
                logger.warning(
                    f"Websocket state:{websocket.application_state},reconnecting..."
                )  # noqa
                await manager.connect(websocket)
    except Exception as e:
        print("line 112", e)

        # template = "An exception of type {0} occurred, Arguments:\n{1!r}"
        # message = template.format(type(e).__name__, e.args)
        # logger.error(message)


# @app.websocket("/ws/{chatroom_name}/{user_name}")
# async def websocket_endpoint(
#     websocket: WebSocket, chatroom_name: str, user_name: str
# ):
#     await manager.connect(websocket)
#     try:

#         chatroom = await get_chatroom(chatroom_name)
#         data = {
#             "content": f"{user_name} has entered the chat",
#             "user": {"username": user_name},
#             "chatroom_name": chatroom_name,
#             "type": "entrance",
#             "new_chatroom_obj": chatroom,
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
#                     await manager.disconnect(websocket)
#                     break
#                 else:
#                     print(f"PLZ WORK {data}")
#                     await upload_message_to_chatroom(data)
#                     logger.info(f"DATA RECEIVED: {data}")
#                     await manager.broadcast(f"{data}")
#             else:
#                 logger.warning(
#                     f"Websocket state:{websocket.application_state},reconnecting..."
#                 )  # noqa
#                 await manager.connect(websocket)
#     except Exception as e:
#         # template = "An exception of type {0} occurred, Arguments: {1!r}"
#         # message = template.format(type(e).__name__, e.args)
#         # logger.error(message)
#         # remove user
#         logger.warning("Disconnecting Websocket")
#         # await remove_user_from_chatroom(
#         #     None, chatroom_name, username=user_name
#         # )
#         chatroom = await get_chatroom(chatroom_name)
#         data = {
#             "content": f"{user_name} has left the chat",
#             "user": {"username": user_name},
#             "chatroom_name": chatroom_name,
#             "type": "dismissal",
#             "new_chatroom_obj": chatroom,
#         }
#         await manager.broadcast(f"{json.dumps(data, default=str)}")
#         await manager.disconnect(websocket)


# from typing import Union

# from fastapi import (
#     Cookie,
#     Depends,
#     FastAPI,
#     Query,
#     WebSocket,
#     websockets,
#     status,
# )
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# html = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>Chat</title>
#     </head>
#     <body>
#         <h1>WebSocket Chat</h1>
#         <form action="" onsubmit="sendMessage(event)">
#             <label>Item ID: <input type="text" id="itemId" autocomplete="off" value="foo"/></label>
#             <label>Chatroom: <input type="text" id="chatroom" autocomplete="off" value="some-key-chatroom"/></label>
#             <button onclick="connect(event)">Connect</button>
#             <hr>
#             <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
#             <button>Send</button>
#         </form>
# <ul id='messages'>
# </ul>
# <script>
# var ws = null;
#     function connect(event) {
#         var itemId = document.getElementById("itemId")
#         var chatroom = document.getElementById("chatroom")
#         ws = new WebSocket("ws://localhost:8000/items/" + itemId.value + "/ws?chatroom=" + chatroom.value);
#         ws.onmessage = function(event) {
#             var messages = document.getElementById('messages')
#             var message = document.createElement('li')
#             var content = document.createTextNode(event.data)
#             message.appendChild(content)
#             messages.appendChild(message)
#         };
#         event.preventDefault()
#     }
#     function sendMessage(event) {
#         var input = document.getElementById("messageText")
#         ws.send(input.value)
#         input.value = ''
#         event.preventDefault()
#     }
# </script>
#     </body>
# </html>
# """


# @app.get("/")
# async def get():
#     return HTMLResponse(html)


# async def get_cookie_or_chatroom(
#     websocket: WebSocket,
#     session: Union[str, None] = Cookie(default=None),
#     chatroom: Union[str, None] = Query(default=None),
# ):
#     if session is None and chatroom is None:
#         raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
#     return session or chatroom


# @app.websocket("/items/{item_id}/ws")
# async def websocket_endpoint(
#     websocket: WebSocket,
#     item_id: str,
#     q: Union[int, None] = None,
#     cookie_or_chatroom: str = Depends(get_cookie_or_chatroom),
# ):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(
#             f"Session cookie or query chatroom value is: {cookie_or_chatroom}"
#         )
#         if q is not None:
#             await websocket.send_text(f"Query parameter q is: {q}")
#         await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")
