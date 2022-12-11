import React, { useState, useEffect, useRef } from "react";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Chat.css";
import Picker from "@emoji-mart/react";
import data from "@emoji-mart/data";
import { Link, useNavigate } from "react-router-dom";
import {useToken, useAuthContext} from "./GetToken";


function Chat() {
    const { token } = useAuthContext();
    const [inputStr, setInputStr] = useState("");
    const [showPicker, setShowPicker] = useState(false);
    const [emojiObj, setEmojiObj] = useState("");
    const [users, setUsers] = useState([]);
    const [chatrooms, setChatrooms] = useState();
    const [selectedChatroom, setSelectedChatroom] = useState("");
    const [getMessages, setGetMessages] = useState([]);
    const [submitted, setSubmitted] = useState(false);
    const [createdRoom, setCreatedRoom] = useState("");
    const [activeUser, setActiveUser] = useState("")
    const [ws, setWs] = useState(null)
    const messagesEndRef = useRef(null)
  // executes all component functions and calls first, then executes useEffects in order.

    useEffect(() => {
      const fetchChatrooms = async () => {
          console.log("---1 fetching Chatrooms")
          const url = `https://${process.env.REACT_APP_CHAT_API_HOST}/api/chatrooms`;
          const response = await fetch(url);
          if (response.ok) {
              const data = await response.json();
              setChatrooms(data);
          }
      }
      fetchChatrooms()
    }, [submitted] )


    useEffect(() => {
        messagesEndRef.current?.scrollIntoView();
    }, [getMessages]);

    const handleClick = (event) => {
        const chatroom = event.target.value
        connectToWebSocket(chatroom)
    }

    const connectToWebSocket = (selectedChatroom) => {
        console.log("---Checking Websocket State")
        const websocket = new WebSocket(`wss://${process.env.REACT_APP_CHAT_API_HOST}/wss/${activeUser}/${selectedChatroom}`);
        websocket.onopen = () => {
            console.log('---Websocket connected to client!');
        };
        websocket.onmessage = (event) => {
            console.log("---On Message")
            const message = JSON.parse(event.data);
            console.log("message:", message)
            const room = message.chatroom_name
            const username = message.user_name
            const content = message.content
            const messageBody = {
                "user_name": username,
                "content": content,
            };
            if (message.hasOwnProperty("type") &&
            (message.type === "entrance")
            ) {
                const chatroom = message.new_chatroom_obj;
                const messages = chatroom.messages;
                const members = chatroom.members;
                setSelectedChatroom(room)
                setUsers(members);
                setGetMessages([...messages])
            } else {
                setGetMessages(current => [...current, messageBody]);
            }
        };
        websocket.onclose = () => {
            console.log("---On Close")

        };
        websocket.onerror = (error) => {
            console.log("---On Error", error.message)
            websocket.close()
        };
        setWs(websocket);
        console.log("---Set ws to equal Websocket")
    }


    const handleSubmit = async (event) => {
        event.preventDefault();
        const message = inputStr;
        const chatroom_name = selectedChatroom;
        const username = activeUser;
        const data = {
            "user_name": username,
            "chatroom_name": chatroom_name,
            "content": message,
        };
        ws.send(JSON.stringify(data))
        setInputStr("");
        setSubmitted(true);
        setShowPicker(false);
        if (submitted === true) {
            setSubmitted(false);
        }
    }


    const handleCreateChatRoom = async (event) => {
        event.preventDefault();
        const chatroom = createdRoom;
        const username = "Bob";
        const data = {
            username: username,
            chatroom_name: chatroom,
        };
        const url = `https://${process.env.REACT_APP_CHAT_API_HOST}/api/chatrooms/`;
        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch(url, fetchConfig);
        if (response.ok) {
            setCreatedRoom("")
            setSubmitted(true);
            if (submitted === true) {
                setSubmitted(false);
            }
        }
    };

    const navigate = useNavigate();
    const [, , logout] = useToken();
    const handleLogout = async (e) => {
        e.preventDefault();
        logout();
        navigate("/");
    }

    let selectedEmoji = emojiObj.native;
    useEffect(() => {
        if (selectedEmoji) {
            setInputStr(inputStr => inputStr + selectedEmoji);
            let added = true;
            if (added) {}
            added = false;
        }
    }, [selectedEmoji]);


    if (token) {
        return (
            <div>
                <div className="window-wrapper">
                    <div className="window-title">
                        <div className="app-title">
                            <div>
                                Chat Catch
                            </div>
                        </div>
                        <div className="expand">
                            <i className="fa fa-expand"></i>
                        </div>
                    </div>
                    <div className="window-area">
                        <div className="members-list">
                            <ul className="">
                                <li
                                className="members-list-title"
                                onChange={(e) => setUsers(e.target.value)}
                                >
                                Members
                                </li>
                                {users?.map(({ date_created, username }) => {
                                    return (
                                        <option
                                        className="member-name-in-list"
                                        key={date_created}
                                        value={username}
                                        >
                                        {username}
                                        </option>
                                    );
                                })};
                            </ul>
                        </div>
                        <div className="chat-area">
                            <div className="chat-area-title">
                                <b>Current Room: </b>
                                <b> {selectedChatroom}</b>
                            </div>
                            <div className="chat-list">
                                    {!getMessages
                                        ? getMessages
                                        : getMessages.map(({ user_name, content }, index) => {
                                            return (
                                                <option
                                                    className="chat-text"
                                                    key={index}
                                                >
                                                    {`${user_name}: ${content}`}
                                                </option>
                                            )
                                        })
                                    }
                                <div ref={messagesEndRef}>
                                </div>
                            </div>
                            <form>
                                <div className="input-area">
                                    {showPicker && (
                                        <Picker data={data} onEmojiSelect={setEmojiObj} />
                                    )}
                                    <div className="input-wrapper">
                                        <input
                                            className="text-input"
                                            onChange={(e) => setInputStr(e.target.value)}
                                            type="text"
                                            value={inputStr}
                                        />
                                        <img
                                            className="emoji-icon"
                                            src="https://icons.getbootstrap.com/assets/icons/emoji-smile.svg"
                                            alt=""
                                            onClick={() => setShowPicker((val) => !val)}
                                        />
                                        <Button
                                            onClick={handleSubmit}
                                            type="submit"
                                            className="send-btn"
                                            variant="secondary"
                                        >
                                            {" "}
                                            Send{" "}
                                        </Button>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <div className="right-tabs">
                            <ul className="tabs-container">
                                <div className="title">
                                <b>Your Chatrooms</b>
                                </div>
                            </ul>
                            <div className="chatroom-list">
                                <ul>
                                    <li onClick={handleClick}>
                                        {chatrooms?.map(({ _id, chatroom_name }) => {
                                            return (
                                                <Link key={_id} value={chatroom_name} style={{textDecoration: 'none'}}>
                                                    <option className="chatroom-name-list"
                                                    >
                                                    {chatroom_name}
                                                    </option>
                                                </Link>
                                            );
                                        })}
                                    </li>
                                </ul>
                                <input
                                    onChange={(e) => setActiveUser(e.target.value)}
                                    className="text"
                                    type="text"
                                />
                            </div>
                            <form>
                                <input
                                    className="add-chat-room"
                                    onChange={(e) => setCreatedRoom(e.target.value)}
                                    type="text"
                                    placeholder="Create Chatroom"
                                    value={createdRoom}
                                />
                                <Button
                                    onClick={handleCreateChatRoom}
                                    className="create-room-btn"
                                    variant="secondary"
                                >
                                Create
                                </Button>
                            </form>
                            <Link to="">
                                <Button
                                    onClick={handleLogout}
                                    className="logout-btn"
                                    variant="outline-secondary"
                                >
                                Logout
                                </Button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        )
    } else {
        return (
            <div className="window-wrapper">
                <p>Chat Catch</p>
                <div className="reminder-message">
                    Sorry, you need to log in to see the chatrooms!
                    <div>
                        <Link className="login-here" to="/">
                            Login here.
                        </Link>
                    </div>
                </div>
            </div>
        )
    }
}

export default Chat;

//                         {/* <div className="members-list">
//                             <ul className="">
//                                 <li */}
//                                 className="members-list-title"
//                                 onChange={(e) => setUsers(e.target.value)}
//                                 >
//                   Members
//                 </li>
//                 {users?.map(({ date_created, username }) => {
//                   return (
//                     <option
//                       className="member-name-in-list"
//                       key={date_created}
//                       value={username}
//                     >
//                       {username}
//                     </option>
//                   );
//                 })}
//                 ;
//               </ul>
//             </div>
//             <div className="chat-area">
//               <div className="chat-area-title">
//                 <b>Current Room: </b>
//                 <b> {selectedChatroom}</b>
//               </div>
//               <div
//                 className="chat-list"
//               >
//                 {!getMessages
//                   ? getMessages
//                   : getMessages.map(({ username, content }, index) => {
//                     return (
//                       <option className="chat-text" key={index}>
//                           {`${username}: ${content}`}
//                         </option>
//                       );
//                     })}
//               <div ref={messagesEndRef}>
//               </div>
//               </div>

//                 <form>
//                   <div className="input-area">
//                     {showPicker && (
//                       <Picker data={data} onEmojiSelect={setEmojiObj} />
//                     )}
//                     <div className="input-wrapper">
//                       <input
//                         className="text-input"
//                         onChange={(e) => setInputStr(e.target.value)}
//                         type="text"
//                         value={inputStr}
//                       />
//                       <img
//                         className="emoji-icon"
//                         src="https://icons.getbootstrap.com/assets/icons/emoji-smile.svg"
//                         alt=""
//                         onClick={() => setShowPicker((val) => !val)}
//                       />
//                       <Button
//                         onClick={handleSubmit}
//                         type="submit"
//                         className="send-btn"
//                         variant="secondary"
//                       >
//                         {" "}
//                         Send{" "}
//                       </Button>
//                     </div>
//                   </div>
//                 </form>
//               </div>

//             <div className="right-tabs">
//                 <ul className="tabs-container">
//                 <div className="title">
//                     <b>Your Chatrooms</b>
//                 </div>
//                 </ul>
//                 <div className="chatroom-list">
//                 <ul>
//                     <li onClick={handleClick}>
//                     {chatrooms?.map(({ _id, chatroom_name }) => {
//                         return (
//                             <a
//                                 href="!#"
//                                 key={_id}
//                                 value={chatroom_name}

//                             ><option className="chatroom-name-list">
//                                 {chatroom_name}</option>
//                             </a>
//                         );
//                     })}
//                     </li>
//                 </ul>
//                 <input
//                         onChange={(e) => setActiveUser(e.target.value)}
//                         className="text"
//                         type="text"
//                     />
//                 </div>
//                 <Link to="/">
//                 <Button className="logout-btn" variant="outline-secondary">
//                     Logout
//                 </Button>
//                 </Link>
//             </div>
//             </div>
//         </div>
//         </div>
//             <div className="right-tabs">
//               <ul className="tabs-container">
//                 <div className="title">
//                   <b>Your Chatrooms</b>
//                 </div>
//               </ul>
//               <div className="chatroom-list">
//                 <ul>
//                   <li onClick={(e) => setSelectedChatroom(e.target.value)}>
//                     {chatrooms?.map(({ _id, chatroom_name }) => {
//                       return (
//                         <Link key={_id} value={chatroom_name}>
//                           <option className="chatroom-name-list">
//                             {chatroom_name}
//                           </option>
//                         </Link>
//                       );
//                     })}
//                   </li>
//                 </ul>
//               </div>
//             <form>
//                 <input
//                     className="add-chat-room"
//                     onChange={(e) => setCreatedRoom(e.target.value)}
//                     type="text"
//                     placeholder="Create Chatroom"
//                     value={createdRoom}
//                 />
//                 <Button
//                     onClick={handleCreateChatRoom}
//                     className="create-room-btn"
//                     variant="secondary"
//                 >
//                     Create
//                 </Button>
//             </form>
//                 <Link to="/">
//                     <Button onClick={handleLogout} className="logout-btn" variant="outline-secondary">
//                         Logout
//                     </Button>
//                 </Link>
//         </div>
//     </div>
//     );
//   } else {
//     return (
//     <div className="window-wrapper">
//       <p>Chat Catch</p>
//       <div className="reminder-message">
//         Sorry, you need to log in to see the chatrooms!
//         <div>
//         <Link className="login-here" to="/">
//           Login here.
//         </Link>
//         </div>
//       </div>
//     </div>
//   )
//   }
// }

// export default Chat;
