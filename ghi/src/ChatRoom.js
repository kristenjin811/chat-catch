import UserList from "./UserList";
import ChatroomList from "./websocket-test";

// const selectedChatroom =

function sendMessage(event){
    let input = messageText
    ws.send(input.value)
    input.value = ""
    event.preventDefault()
};

const Chat = (data) => {
    return (
      <div>

        <form action="" onSubmit={sendMessage(event)}>
          {/* <ChatroomList />
          <UserList /> */}
          User: <input type="text" id="username" autoComplete="off" />
          <hr />
          <label>
            Message: <input type="text" id="messageText" autoComplete="off" />
          </label>
          <button>Send</button>
        </form>
        <ul id="messages"></ul>
        {/* <script>{
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

        </script> */}

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


// <div className="container overflow-hidden mt-5">
//     <h1 className="text-center">Welcome to {selectedChatroom} Chat</h1>
//         <select
//           className="form-select"
//           name="chatroom"
//           id="chatroom"
//           value=""
//           onChange={(e) => setSelectedChatroom(e.target.value)}
//         >
//           <option>{selectedChatroom}</option>
//           {chatrooms?.map(({ _id, chatroom_name }) => {
//             return (
//               <option key={_id} value={chatroom_name}>
//                 {chatroom_name}
//               </option>
//             );
//           })}
//         </select>
//         <button
//           onClick={() =>
//             navigate(
//               `/${selectedChatroom}`
//             )
//           }
//           className="btn btn-primary"
//         >
//           Choose Chatroom
//         </button>
//       </div>

// <div className="shadow p-4 mt-4">
// //           <h1 className="text-center">Create a Message</h1>
