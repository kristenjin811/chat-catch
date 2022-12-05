import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import React, { useState } from 'react'
import EmojiPicker from './EmojiPicker'
import Button from 'react-bootstrap/Button';
import ListGroup from 'react-bootstrap/ListGroup';
import 'bootstrap/dist/css/bootstrap.min.css';

import "./Chat.css"

function Chat() {
  const [inputStr, setInputStr] = useState('')
  const [showPicker, setShowPicker] = useState(false)


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
              <li className="members-list-title">Members</li>
              <li className="member-name-in-list">Cucu Ionel</li>
              <li className="member-name-in-list">Jan Dvořák</li>
              <li className="member-name-in-list">Clark Ken</li>
              <li className="member-name-in-list">Ioana Marcu</li>
            </ul>
          </div>
          <div className="chat-area">
            <div className="chat-area-title">
              <b>Chatroom #1</b>
            </div>
            <div className="chat-list"></div>
            <div className="input-area">
              <div className="input-wrapper">
                <input
                  value={inputStr}
                  onChange={(e) => setInputStr(e.target.value)}
                  className="text"
                  type="text"
                  defaultValue=""
                />
                <img
                  className="emoji-icon"
                  src="https://icons.getbootstrap.com/assets/icons/emoji-smile.svg"
                  onClick={() => setShowPicker((val) => !val)}
                />
                {showPicker && (
                  <EmojiPicker
                    pickerStyle={{ width: "100%" }}
                    onEmojiClick={onEmojiClick}
                  />
                )}
              </div>
              <Button className="send-btn" variant="secondary">
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
                <div class="season_tab">
                  <input type="radio" id="tab-2" name="tab-group-1" />
                  <label htmlFor="tab-2">Chatroom 1</label>

                  <div class="season_content">
                    <span>tabik 2</span>
                  </div>
                </div>

                <div class="season_tab">
                  <input type="radio" id="tab-3" name="tab-group-1" />
                  <label htmlFor="tab-3">Chatroom 2</label>

                  <div class="season_content">
                    <span>Chatroom 2</span>
                  </div>
                </div>
                <div class="season_tab">
                  <input type="radio" id="tab-4" name="tab-group-1" />
                  <label htmlFor="tab-4">chatroom 3</label>

                  <div class="season_content">
                    <span>chatroom 3</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* <Row id="chat">
          <Col>
            <div className="current-chatroom-name">Chatroom Name</div>
            <div className="chat-box">chat box</div>
          </Col>
        </Row>
        <Row id="text-area">
          <Col>
            <div className="picker-container">
              <input
                className="input-style"
                value={inputStr}
                onChange={e => setInputStr(e.target.value)} />
              <img
                className="emoji-icon"
                src="https://icons.getbootstrap.com/assets/icons/emoji-smile.svg"
                onClick={() => setShowPicker(val => !val)} />
              {showPicker && <EmojiPicker
                pickerStyle={{ width: '100%' }}
                onEmojiClick={onEmojiClick} />}
              <Button className="send-button" variant="dark">Send</Button>
            </div>
          </Col>
        </Row> */}
    </>
  );
}

export default Chat
