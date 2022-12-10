from fastapi import (
    WebSocket,
)

# from starlette.websockets import WebSocketState

# import os
# import json
from datetime import datetime, timezone


def timestamp():
    timestamp = datetime.now(timezone.utc).isoformat()
    return str(timestamp)


class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    async def connect(
        self, websocket: WebSocket, user_name: str, chatroom_name: str
    ):
        await websocket.accept()
        print("---Accepted Connection!")
        if user_name not in self.active_connections:
            self.active_connections[user_name] = {}
        self.active_connections[user_name][chatroom_name] = websocket

    async def disconnect(self, user_name: str, chatroom_name: str):
        print("---Disconnecting websocket")
        if (
            user_name in self.active_connections
            and chatroom_name in self.active_connections[user_name]
        ):
            ws = self.active_connections[user_name].pop(chatroom_name)
            ws.close()

    async def send_personal_message(self, message: str, websocket: WebSocket):
        print("---Sending Personal Message")
        await websocket.send_text(message)

    async def broadcast(
        self, message: str, user_name: str, chatroom_name: str
    ):
        for user_name in self.active_connections:
            if chatroom_name in self.active_connections[user_name]:
                ws = self.active_connections[user_name][chatroom_name]
                await ws.send_text(message)


# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: List[WebSocket] = []
#         self.current_message_id = 0

#     async def connect(self, websocket: WebSocket, client_id: int):
#         print("Accepting Connection")
#         await websocket.accept()
#         print("Accepted!")
#         self.active_connections.append(websocket)
#         await self.send_personal_message(
#             "Welcome!",
#             client_id,
#             websocket,
#         )

#     def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)

#     async def send_personal_message(
#         self,
#         message: str,
#         client_id: int,
#         websocket: WebSocket,
#     ):
#         payload = json.dumps(
#             {
#                 "client_id": client_id,
#                 "content": message,
#                 "timestamp": timestamp(),
#                 "message_id": self.next_message_id(),
#             }
#         )
#         await websocket.send_text(payload)

#     async def broadcast(self, message: str, user_name: str):
#         payload = json.dumps(
#             {
#                 "user_name": user_name,
#                 "content": message,
#                 "timestamp": timestamp(),
#                 "message_id": self.next_message_id(),
#             }
#         )
#         print("active connections:", len(self.active_connections))
#         for connection in self.active_connections:
#             await connection.send_text(payload)

#     def next_message_id(self):
#         self.current_message_id += 1
#         return self.current_message_id
