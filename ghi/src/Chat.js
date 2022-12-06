import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import React, { useState , useEffect } from 'react'
import EmojiPicker from './EmojiPicker'
import Button from 'react-bootstrap/Button';
import ListGroup from 'react-bootstrap/ListGroup';
import 'bootstrap/dist/css/bootstrap.min.css';
import UserList from './UsersList'
import "./Chat.css"

function Chat() {
  const [inputStr, setInputStr] = useState('')
  const [showPicker, setShowPicker] = useState(false)
  const [users, setUsers] = useState([]);
  const [chatrooms, setChatrooms] = useState([]);
  const [selectedChatroom, setSelectedChatroom] = useState("");
  const [getMessages, setGetMessages] = useState("");



  useEffect(() => {
    const fetchMessages = async () => {
      const url = "http://localhost:8000/api/messages"
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setGetMessages(data)
      }
    };
    fetchMessages();
  }, [])

  useEffect(() => {
    const fetchUsers = async () => {
      const url = `http://localhost:8000/api/chatrooms/${selectedChatroom}`
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setUsers(data.members);

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
     const username = "Frank"

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
     if (response.ok) {
       setInputStr("");

     }
   };


  const onEmojiClick = (event, emojiObject) => {
    setInputStr(prevInput => prevInput + emojiObject.emoji)
    setShowPicker(false)

  };




  return (
    <>
      {/* <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"/> */}

      <div className="window-wrapper">
        <div className="window-title">
          <div className="app-title">
            <p>Chat Catch</p>
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
            </ul>
          </div>
          <div className="chat-area">
            <div className="chat-area-title">
              <b>Current Room: </b>
              <b> {selectedChatroom}</b>
            </div>
            <div className="chat-list">
              {/* {getMessages?.map(({ _id, message }) => {
                return (
                  <option
                    key={_id}
                    value={message}
                  >
                    {message}
                  </option>
                );
              })} */}
            </div>
            <div className="input-area">
              <div className="input-wrapper">
                <input className="text" type="text" defaultValue=""/>
                <img
                  className="emoji-icon"
                  src="https://icons.getbootstrap.com/assets/icons/emoji-smile.svg"
                  onClick={() => setShowPicker(val => !val)} />
                {showPicker && <EmojiPicker
                  pickerStyle={{ width: '100%' }}
                  onEmojiClick={onEmojiClick} />}
              </div>
              <Button
                onClick={handleSubmit}
                className="send-btn"
                variant="secondary"
              >
                Send
              </Button>
            </div>
          </div>
          <div className="right-tabs">
            <ul className="tabs-container">
              <div className="title">
                <b>Your chatrooms</b>
              </div>
            </ul>
            <div className="chatroom-list">
              <div className="season_tabs">
                <div className="season_tab">
                  <ul>
                    <li onClick={(e) => setSelectedChatroom(e.target.value)}>
                      {chatrooms?.map(({ _id, chatroom_name }) => {
                        return (
                          <option
                            className="table table-striped "
                            key={_id}
                            value={chatroom_name}
                          >
                            {chatroom_name}
                          </option>
                        );
                      })}
                    </li>
                  </ul>

                  <input type="radio" id="tab-2" name="tab-group-1" />
                  <label htmlFor="tab-2">Chatroom 1</label>

                  <div className="season_content">
                    <span>Chatroom 1</span>
                  </div>
                </div>

                <div className="season_tab">
                  <input type="radio" id="tab-3" name="tab-group-1" />
                  <label htmlFor="tab-3">Chatroom 2</label>

                  <div className="season_content">
                    <span>Chatroom 2</span>
                  </div>
                </div>
                <div className="season_tab">
                  <input type="radio" id="tab-4" name="tab-group-1" />
                  <label htmlFor="tab-4">chatroom 3</label>

                  <div className="season_content">
                    <span>chatroom 3</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* </div> */}
    </>
  );
}

export default Chat;
{
  chatrooms?.map(({ _id, chatroom_name }) => {
    return (
      <option className="table table-striped " key={_id} value={chatroom_name}>
        {chatroom_name}
      </option>
    );
  });
}
