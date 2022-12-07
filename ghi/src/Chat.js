
import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";
import UserList from "./UsersList";
import "./Chat.css";
import Picker from "@emoji-mart/react";
import data from "@emoji-mart/data";
import {Link} from 'react-router-dom';

function Chat() {
  const [inputStr, setInputStr] = useState("");
  const [showPicker, setShowPicker] = useState(false);
  const [emojiObj, setEmojiObj] = useState("");
  const [users, setUsers] = useState([]);
  const [chatrooms, setChatrooms] = useState([]);
  const [selectedChatroom, setSelectedChatroom] = useState("");
  const [getMessages, setGetMessages] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [emojiStr, setEmojiStr] = useState(null);

  useEffect(() => {
    const fetchMessages = async () => {
      const url = "http://localhost:8000/api/messages";
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        // console.log(data);
        setGetMessages(data);
      }
    };
    fetchMessages();
  }, [submitted]);
  // , [getMessages]);

  useEffect(() => {
    const fetchUsers = async () => {
      const url = `http://localhost:8000/api/chatrooms/${selectedChatroom}`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        // console.log(data.messages);
        setUsers(data.members);
        // setGetMessages(data.messages)

      }
    };
    fetchUsers();
  }, [selectedChatroom]);

  useEffect(() => {
     const fetchChatrooms = async () => {
       const url = "http://localhost:8000/api/chatrooms";
       const response = await fetch(url);
       if (response.ok) {
         const data = await response.json();
         setChatrooms(data);
       }
     };
     fetchChatrooms();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const message = inputStr
    const chatroom_name = selectedChatroom;
    const username = "Frank";
    const data = { username, message, chatroom_name };
    const url = "http://localhost:8000/api/messages";
    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(url, fetchConfig);
    console.log("response::", response);
    if (response.ok) {
      setInputStr("");
      setSubmitted(true);
      setEmojiStr("");
      setShowPicker(false);
      if(submitted == true) {
        setSubmitted(false);
      }
    }
  };

  let selectedEmoji = emojiObj.native;
  useEffect(() => {
        setEmojiStr(selectedEmoji)
       if (selectedEmoji){
         setInputStr(inputStr + selectedEmoji);
         let added = true
        //  emojiObj = null;
         console.log("did this add:::::", added)
         if (added){

         }
         added = false
       }
  },[selectedEmoji]);


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
                : getMessages.map(({ _id, message }) => {
                  return (
                    <option key={_id} value={message}>
                        {message}
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
                <li onClick={(e) => setSelectedChatroom(e.target.value)}>
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
