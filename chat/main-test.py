from typing import Union

from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    # status,
)


# from websockets.exceptions import WebSocketException

app = FastAPI()


async def get_cookie_or_chatroom(
    websocket: WebSocket,
    session: Union[str, None] = Cookie(default=None),
    chatroom: Union[str, None] = Query(default=None),
):
    # if session is None and chatroom is None:
    #     raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
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
        await websocket.send_text(
            f"Message text was: {data}, for item ID: {item_id}"
        )
