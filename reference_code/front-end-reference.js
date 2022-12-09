/*
ON PRESSING ENTER INSTEAD OF HITTING SEND BUTTON
onEnterHandler = (event) => {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
      // Trigger the button element with a click
      event.preventDefault();
      this.onClickHandler(event);
    }
  };
--------------------------------------------------
SCROLL TO BOTTOM FUNCTION
  scrollToBottom() {
    animateScroll.scrollToBottom({
      containerId: "message-list",
      duration: "1ms",
    });
  }
-------------------------------------------------
    ON MESSAGE RECEIVED FROM BACKEND - PARSE THE JSON (MESSAGE),
    IF MESSAGE TYPE IS DISMISSAL OR ENTRANCE,
    SET SELECTEDCHATROOM
    ELSE CREATES NEW MESSAGE AND PUSHES TO MESSAGES ARRAY IN STATE
    THEN SCROLLS TO THE BOTTOM OF THE TEXT WINDOW

    ws.onmessage = (event) => {
        let message = JSON.parse(event.data);
        if (
        message.hasOwnProperty("type") &&
        (message.type === "dismissal" ||
            message.type === "entrance")
        ) {
            this.setState({
                ...message["new_room_obj"],
            });
        } else {
            let message_body = {
                content: message["content"],
                user: message["user"],
            };
            let messages_arr = this.state.messages;
            messages_arr.push(message_body);
            this.setState(
                { messages: messages_arr },
                this.scrollToBottom
            );
        }
    };
------------------------------------------------------
DISPLAYING MESSAGES IN TEXTBOX WITH TEXTWRAP,
LEFT/RIGHT ORIENTATION AND DEFINING L/R MARGINS
https://github.com/jmoussa/chat-app-fe/blob/develop/src/components/ChatModule.js
LINES 265 - END



------------------------------------------------------


*/
