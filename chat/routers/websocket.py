from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
    Depends,
)
import os
from jose import jwt
import json
from datetime import datetime, timezone

router = APIRouter()


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def get_jwt():
    return jwt


class ConnectionManager:
    def __init__(self):
        self.active_connections = dict()
        self.current_message_id = 0

    async def connect(self, websocket: WebSocket, jwt_jose):
        await websocket.accept()
        token_data = jwt_jose.decode(
            websocket.query_params["token"],
            os.environ["SIGNING_KEY"],
            algorithms=["HS256"],
        )

        username = token_data["account"]["username"]
        self.active_connections[username] = websocket
        await self.send_personal_message(
            "Welcome!",
            username,
            websocket,
        )
        return username

    def disconnect(self, username: str):
        del self.active_connections[username]

    async def send_personal_message(
        self,
        message: str,
        username: str,
        websocket: WebSocket,
    ):
        payload = json.dumps(
            {
                "username": username,
                "content": message,
                "timestamp": timestamp(),
                "message_id": self.next_message_id(),
            }
        )
        await websocket.send_text(payload)

    async def broadcast(self, message: str, username: str):
        payload = json.dumps(
            {
                "username": username,
                "content": message,
                "timestamp": timestamp(),
                "message_id": self.next_message_id(),
            }
        )
        print("active connections:", len(self.active_connections))
        for connection in self.active_connections.values():
            await connection.send_text(payload)

    def next_message_id(self):
        self.current_message_id += 1
        return self.current_message_id


manager = ConnectionManager()


@router.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, jwt_jose=Depends(get_jwt)):

    username = await manager.connect(websocket, jwt_jose)
    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(message, username)
    except WebSocketDisconnect:
        print("Disconnect", username)
        manager.disconnect(username)
        await manager.broadcast("Disconnected", username)
