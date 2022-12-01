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
    return datetime.now(timezone.utc).isoformat()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.current_message_id = 0

    async def connect(self, websocket: WebSocket, client_id: int):
        await websocket.accept()
        self.active_connections.append(websocket)
        await self.send_personal_message(
            "Welcome!",
            client_id,
            websocket,
        )

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(
        self,
        message: str,
        client_id: int,
        websocket: WebSocket,
    ):
        payload = json.dumps(
            {
                "client_id": client_id,
                "content": message,
                "timestamp": timestamp(),
                "message_id": self.next_message_id(),
            }
        )
        await websocket.send_text(payload)

    async def broadcast(self, message: str, client_id: int):
        payload = json.dumps(
            {
                "client_id": client_id,
                "content": message,
                "timestamp": timestamp(),
                "message_id": self.next_message_id(),
            }
        )
        print("active connections:", len(self.active_connections))
        for connection in self.active_connections:
            await connection.send_text(payload)

    def next_message_id(self):
        self.current_message_id += 1
        return self.current_message_id


manager = ConnectionManager()


@router.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):

    username = await manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(message, username)
    except WebSocketDisconnect:
        print("Disconnect", username)
        manager.disconnect(username)
        await manager.broadcast("Disconnected", username)
