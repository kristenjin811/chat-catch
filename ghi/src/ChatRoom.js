import UserList from "./UserList";
import ChatroomList from "./websocket-test";

const Chat = () => {
    return (
      <div>
        <form action="" onsubmit="sendMessage(event)">
          <ChatroomList />
          <UserList />
          <button onclick="connect(event)">Connect</button>
          <hr />
          <label>
            Message: <input type="text" id="messageText" autocomplete="off" />
          </label>
          <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>{
        let ws = null;
	        function connect(event) {
		    ws = new WebSocket("ws://localhost:8000/chat/ws?chatroom=" + selectedChatroom);
		    ws.onmessage = function(event) {
                let messages = <get chatroom.messages>
			    let message = <?>
			    let content = <input ?>
			    message.appendChild(content)
			    messages.appendChild(message)
		};
		event.preventDefault()
	    }
	    function sendMessage(event) {
		    let input = <messageText>
		    ws.send(input.value)
		    input.value = ""
		    event.preventDefault()
        }
        </script>
      </div>
    );
};

export default Chat;

// import { useState, useEffect } from "react";

// function checkWebSocket(username, roomname) {
//   if (client === null || client.readyState === WebSocket.CLOSED) {
//     client = new WebSocket(
//       "ws://localhost:8000/ws/" + roomname + "/" + username
//     );
//   }
//   return client;
// }

// const ChatModule = () => {
//     const [messages, setMessages] = useState ([])
//     const [messageDraft, setMessageDraft] = useState ("")

//     onInputChange(event) {
//         useEffect (messageDraft, setMessages)
//     }

//     checkWebSocketConnection(){
//         if (client === null || client.readyState === WebSocket.CLOSED){
//             client = new WebSocket(
//                 "ws://localhost:8000/ws/" + selectedChatroom +
//                 "/" +
//                 selectedUser

//             )
//         }
//     }

//     useEffect(() => {

//     })
// }
