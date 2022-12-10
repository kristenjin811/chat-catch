import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Chat.css";
import Picker from "@emoji-mart/react";
import data from "@emoji-mart/data";
import {Link} from 'react-router-dom';

function Chat() {
    const [inputStr, setInputStr] = useState("");
    const [showPicker, setShowPicker] = useState(false);
    const [emojiObj, setEmojiObj] = useState("");
    const [users, setUsers] = useState([]);
    const [chatrooms, setChatrooms] = useState();
    const [selectedChatroom, setSelectedChatroom] = useState("");
    const [getMessages, setGetMessages] = useState([]);
    const [submitted, setSubmitted] = useState(false);
    const [emojiStr, setEmojiStr] = useState(null);
    const [activeUser, setActiveUser] = useState("")
    const [ws, setWs] = useState(null)
  // executes all component functions and calls first, then executes useEffects in order.

    const fetchChatrooms = async () => {
        console.log("---1 fetching Chatrooms")
        const url = "http://localhost:8000/api/chatrooms";
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            setChatrooms(data);
        }
        };
    if (!chatrooms) {
        fetchChatrooms()
        console.log("---2 Fetched Chatrooms")
    }

    const handleClick = (event) => {
        const chatroom = event.target.value
        console.log("------chatroom_name", chatroom)
        connectToWebSocket(chatroom)
    }

    const connectToWebSocket = (selectedChatroom) => {
        console.log("---Checking Websocket State")
        const websocket = new WebSocket(`ws://localhost:8000/ws/${activeUser}/${selectedChatroom}`);
        websocket.onopen = () => {
            console.log('---Websocket connected to client!');
        };
        websocket.onmessage = (event) => {
            console.log("---On Message")
            let message = JSON.parse(event.data);
            console.log("message:", message)
            const room = message.chatroom_name
            const username = message.user_name
            const content = message.content
            let messageBody = {
                "user_name": username,
                "content": content,
            };
            if (message.hasOwnProperty("type") && message.type === "entrance")
             {
                const chatroom = message.new_chatroom_obj;
                const messages = chatroom.messages;
                const members = chatroom.members;
                setSelectedChatroom(room);
                setUsers(members);
                //how to save all new messages to
                setGetMessages([...messages]);
            } else {
                // setGetMessages([...messages, messageBody]);
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
        const message = inputStr
        const chatroom_name = selectedChatroom;
        const username = activeUser;
        const data = {
            'user_name': username,
            'chatroom_name': chatroom_name,
            'content': message,
        };
        ws.send(JSON.stringify(data))
        setInputStr("");
        setSubmitted(true);
        setEmojiStr("");
        setShowPicker(false);
        if(submitted === true) {
            setSubmitted(false);
        }
    };

    let selectedEmoji = emojiObj.native;
    useEffect(() => {
            setEmojiStr(selectedEmoji)
        if (selectedEmoji){
            setInputStr(inputStr + selectedEmoji);
            let added = true
            //  emojiObj = null;
            // console.log("did this add:::::", added)
            if (added){
                added = false
            }
        }
    },[selectedEmoji, inputStr]);



    return (
        <div>
        <div className="window-wrapper">
            <div className="window-title">
            <div className="app-title">
                <div>Chat Catch</div>
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
                {getMessages.length === 0
                    ? getMessages
                    : getMessages.map(({ content, user_name }, index) => {
                    return (
                        <option key={index}>
                            {`${user_name}:${content}`}
                        </option>
                        );
                    })}
                </div>
                <form>
                <div className="input-area">
                    {showPicker && (
                    <Picker data={data} onEmojiSelect={setEmojiObj} />
                    )}
                    <div className="input-wrapper">
                    <input
                        onChange={(e) => setInputStr(e.target.value)}
                        className="text"
                        type="text"
                        value={inputStr}
                        />
                    <img
                        className="emoji-icon"
                        src="https://icons.getbootstrap.com/assets/icons/emoji-smile.svg"
                        onClick={() => setShowPicker((val) => !val)}
                        />
                    <Button
                        onClick={handleSubmit}
                        type="submit"
                        className="send-btn"
                        variant="secondary"
                    >
                        {/* {" "} */}
                        Send

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
                        <a
                            key={_id}
                            value={chatroom_name}

                        ><option className="chatroom-name-list">
                            {chatroom_name}</option>
                        </a>

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
                <Link to="/">
                <Button className="logout-btn" variant="outline-secondary">
                    Logout
                </Button>
                </Link>
            </div>
            </div>
        </div>
        </div>

    );
}

export default Chat;