from fastapi import WebSocket
# from datetime import datetime, timezone

# def timestamp():
#     timestamp = datetime.now(timezone.utc).isoformat()
#     return str(timestamp)

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
