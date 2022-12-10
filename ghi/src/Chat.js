import React, { useState, useRef, useEffect } from "react";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Chat.css";
import Picker from "@emoji-mart/react";
import data from "@emoji-mart/data";
import { Link, useNavigate } from "react-router-dom";
import {useToken, useAuthContext } from "./GetToken";


function Chat() {
  const { token } = useAuthContext();
  const [inputStr, setInputStr] = useState("");
  const [showPicker, setShowPicker] = useState(false);
  const [emojiObj, setEmojiObj] = useState("");
  const [users, setUsers] = useState([]);
  const [chatrooms, setChatrooms] = useState([]);
  const [selectedChatroom, setSelectedChatroom] = useState("");
  const [getMessages, setGetMessages] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [createdRoom, setCreatedRoom] = useState("");
  const messagesEndRef = useRef(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView();
  }, [getMessages]);

  useEffect(() => {
    const fetchUsers = async () => {
      const url = `http://localhost:8000/api/chatrooms/${selectedChatroom}`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        console.log(data.messages);
        setUsers(data.members);
        setGetMessages(data.messages);
      }
    };
    fetchUsers();
  }, [selectedChatroom, submitted]);

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
  }, [submitted]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const message = inputStr;
    const chatroom_name = selectedChatroom;
    const username = "Bob";
    const data = {
      username: username,
      chatroom_name: chatroom_name,
      message: message,
    };
    const url = `http://localhost:8000/api/chatrooms/${selectedChatroom}`;
    const fetchConfig = {
      method: "PUT",
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
      setShowPicker(false);
      if (submitted === true) {
        setSubmitted(false);
      }
    }
  };

  const handleCreateChatRoom = async (event) => {
    event.preventDefault();
    const chatroom = createdRoom;
    const username = "Bob";
    const data = {
      username: username,
      chatroom_name: chatroom,
    };
    const url = `http://localhost:8000/api/chatrooms/`;
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
      if (added) {
      }
      added = false;
    }
  }, [selectedEmoji]);


  if (token) {
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
                })}
                ;
              </ul>
            </div>
            <div className="chat-area">
              <div className="chat-area-title">
                <b>Current Room: </b>
                <b> {selectedChatroom}</b>
              </div>
              <div
                className="chat-list"
              >
                {!getMessages
                  ? getMessages
                  : getMessages.map(({ username, content }, index) => {
                    return (
                      <option className="chat-text" key={index}>
                          {`${username}: ${content}`}
                        </option>
                      );
                    })}
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
                  <li onClick={(e) => setSelectedChatroom(e.target.value)}>
                    {chatrooms?.map(({ _id, chatroom_name }) => {
                      return (
                        <Link key={_id} value={chatroom_name}>
                          <option className="chatroom-name-list">
                            {chatroom_name}
                          </option>
                        </Link>
                      );
                    })}
                  </li>
                </ul>
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
              <Link to="/">
                <Button onClick={handleLogout} className="logout-btn" variant="outline-secondary">
                  Logout
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
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
