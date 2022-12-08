from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
    # Depends,
)

# import os
import json
from datetime import datetime, timezone
from typing import List

router = APIRouter()


def timestamp():
    timestamp = datetime.now(timezone.utc).isoformat()
    return str(timestamp)


# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: List[WebSocket] = []
#         self.current_message_id = 0

#     async def connect(self, websocket: WebSocket, user_name: str):
#         await websocket.accept()
#         username = user_name
#         self.active_connections.append(websocket)
#         await self.send_personal_message(
#             "Welcome!",
#             username,
#             websocket,
#         )

#     def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)

#     async def send_personal_message(
#         self,
#         message: str,
#         user_name: str,
#         websocket: WebSocket,
#     ):
#         payload = json.dumps(
#             {
#                 "username": user_name,
#                 "content": message,
#                 "timestamp": timestamp(),
#                 "message_id": self.next_message_id(),
#             },
#             default=str,
#         )
#         await websocket.send_text(payload)

#     async def broadcast(self, data):
#         message = json.loads(data)
#         user_name = message["user_name"]
#         content = message["content"]
#         payload = json.dumps(
#             {
#                 "username": user_name,
#                 "content": content,
#                 "timestamp": timestamp(),
#                 "message_id": self.next_message_id(),
#             },
#             default=str,
#         )
#         print("active connections:", len(self.active_connections))
#         for connection in self.active_connections:
#             await connection.send_text(payload)

#     def next_message_id(self):
#         self.current_message_id += 1
#         return self.current_message_id


# manager = ConnectionManager()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        print("---Accepted Connection!")
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        print("---Disconnecting websocket")
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        print("---Sending Personal Message")
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        print("---Broadcasting Message")
        for connection in self.active_connections:
            await connection.send_text(message)
