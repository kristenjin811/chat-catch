from typing import Union

from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    status,
)
from fastapi.responses import HTMLResponse

# from websockets.exceptions import WebSocketException

app = FastAPI()

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
#         <ul id='messages'>
#         </ul>
#         <script>
#         var ws = null;
#             function connect(event) {
#                 var itemId = document.getElementById("itemId")
#                 var chatroom = document.getElementById("chatroom")
#                 ws = new WebSocket("ws://localhost:8000/items/" + itemId.value + "/ws?chatroom=" + chatroom.value);
#                 ws.onmessage = function(event) {
#                     var messages = document.getElementById('messages')
#                     var message = document.createElement('li')
#                     var content = document.createTextNode(event.data)
#                     message.appendChild(content)
#                     messages.appendChild(message)
#                 };
#                 event.preventDefault()
#             }
#             function sendMessage(event) {
#                 var input = document.getElementById("messageText")
#                 ws.send(input.value)
#                 input.value = ''
#                 event.preventDefault()
#             }
#         </script>
#     </body>
# </html>
# """
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
