import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import React, { useState, useEffect } from "react";
import EmojiPicker from "./EmojiPicker";
import Button from "react-bootstrap/Button";
import ListGroup from "react-bootstrap/ListGroup";
import "bootstrap/dist/css/bootstrap.min.css";
import UserList from "./UsersList";
import "./Chat.css";
import Picker from "@emoji-mart/react";
import data from "@emoji-mart/data";

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

  useEffect((event) => {
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

  //  setEmoji(result)[]
  // const apple = emoji.native;
  // setResult(apple);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const message = inputStr
    //  const emoji = emoji.native;
    const chatroom_name = selectedChatroom;
    const username = "Frank";
  const handleSubmit = async (event) => {
    event.preventDefault();
    const message = inputStr
    const chatroom_name = selectedChatroom;
    const username = "Frank"

    const data = { username, message, chatroom_name };
    const data = { username, message, chatroom_name };

    const url = "http://localhost:8000/api/messages";
    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },

    };
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
     }
   };

  const onEmojiClick = (event, emojiObject) => {
    setInputStr(prevInput => prevInput + emojiObject.emoji)
    setShowPicker(false)

  };

  // const onEmojiClick = (event, emoji) => {
  //   // setEmoji(emoji.native)
  //   console.log("helloooo", emoji.native);
  //   // setShowPicker(false)
  // };

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


      //  setInputStr(inputStr + " " + emojiStr);

        //  setInputStr(inputStr + emojiStr);
        //  inputStr = inputStr + emojiStr;

      //  setInputStr(inputStr + " " + emojiStr);

  },[selectedEmoji]);
  // console.log("result::", emojiStr)


  return (
    <>
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
                  {showPicker && (
                    // <EmojiPicker
                    //   pickerStyle={{ width: "100%" }}
                    //   onChange={(event) => onEmojiClick(event.target.value)}
                    // onEmojiClick={setEmoji}
                    // />
                    <Picker data={data} onEmojiSelect={setEmojiObj} />
                  )}
                  {/* {console.log("PLEASE HELP ME", data)} */}
                </div>
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
            </form>
          </div>

          <div className="right-tabs">
            <ul className="tabs-container">
              <div className="title">
                <b>Your Chatrooms</b>
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

                  {/* <input type="radio" id="tab-2" name="tab-group-1" />
                  <label htmlFor="tab-2">Chatroom 1</label>

                  <div className="season_content">
                    <span>Chatroom 1</span>
                  </div> */}
                </div>

                {/* <div className="season_tab">
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
                  </div> */}
                </div>
              </div>
            </div>
            <div>
          </div>
        </div>
      {/* </div> */}
    </>
  );
}

export default Chat;
// { chatrooms?.map(({ _id, chatroom_name }) => {
//     return (
//       <option className="table table-striped " key={_id} value={chatroom_name}>
//         {chatroom_name}
//       </option>
//     );
//   });
// }
