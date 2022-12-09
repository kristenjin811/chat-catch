import {useState, useEffect} from 'react'

const Chatpage = () => {
    const [chatrooms, setChatrooms] = useState([]);
    const [selectedChatroom, setSelectedChatroom] = useState(null); //what is the datatype?
    const [user, setUser] = useState("jared");

    const selectChatroom = (selectedChatroomName) => {
        const selectedChatroomObj = chatrooms.find(
            (chatroom) => chatroom.chatroom_name === selectedChatroomName,
        );
        setSelectedChatroom(selectedChatroomObj);
    }

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

    return (
        <div>
            <div className="container overflow-hidden mt-5">
                <select
                    className="form-select"
                    name="chatroom"
                    id="chatroom"
                    value=""
                    onChange={(e) => selectChatroom(e.target.value)}
                >
                    <option>Select a Chatroom</option>
                    {chatrooms?.map(({_id, chatroom_name}) => {
                        return (
                        <option key={_id} value={chatroom_name}>
                            {chatroom_name}
                        </option>
                        );
                    })}
                </select>
                <label>User:
                    <input
                        type="text"
                        id="user"
                        autoComplete="off"
                        defaultValue={user}
                        onChange={(e) => setUser(e.target.value)}
                    />
                </label>
                <h1>{selectedChatroom && `Welcome to ${selectedChatroom.chatroom_name}!`}</h1>
            </div>
            { selectedChatroom && user &&
                <Messages
                    selectedChatroomName={selectedChatroom.chatroom_name}
                    messages={selectedChatroom.messages}
                    user={user}
                />
            }
        </div>
    );
}


const Messages = ({selectedChatroomName, user}) => {
    const [ws, setWs] = useState(null)
    const [messageDraft, setMessageDraft] = useState("");
    const [messages, setMessages] = useState([]);

    // async function addMessage(event){
    //     event.preventDefault();
    //     // ws.send({"username": user, "message": message})
    // }

    // useEffect(() => {
    //     const connectToWebSocket = () => {
    //         if (!ws || ws?.readyState === WebSocket.CLOSED) {
    //             const websocket = new WebSocket(`ws://localhost:8000/ws/${selectedChatroomName}/${user}`);

    //             websocket.onopen = () => {
    //                 // websocket.send("{'message': 'Connected to client!'}");
    //                 console.log('Websocket connected to client!');
    //             }

    //             websocket.onmessage = function(event) {
    //                 let incomingMessage = JSON.parse(event.data);
    //                 // if (incoming_message.hasOwnProperty("type") &&
    //                 //     (incoming_message.type === "dismissal" ||
    //                 //     incoming_message.type === "entrance")
    //                 //     ) {
    //                 //         setSelectedChatroom(incoming_message.new_room_obj)
    //                 //         setUser
    //                 //     }
    //                 let messageBody = {
    //                   content: incomingMessage["content"],
    //                   user: incomingMessage["user"],
    //                 };
    //                 getMessages.push(messageBody)


    //             };

                // websocket.onclose = () => {setTimeout(connectToWebSocket, 1000)}
                setWs(websocket);
            }
        };
        connectToWebSocket();
    }, [selectedChatroomName, user, ws])

    const handleSubmit = (event) => {
        event.preventDefault();
        const username = user
        const input = messageDraft
        if (input.length > 0) {
            const message_obj = {
                content: input,
                username: username,
                chatroom_name: selectedChatroomName,
            };
            if (ws !== null) {
                ws.send(JSON.stringify(message_obj));
                setMessageDraft("") //scroll to bottom
            } else {
                connectToWebSocket();
                ws.send(JSON.stringify(message_obj));
                setMessageDraft("") //scroll to bottom;
            }
        }
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <hr />
                <label>
                    Message:
                    <input
                        type="text"
                        id="messageText"
                        autoComplete="off"
                        defaultValue={messageDraft}
                        onChange={(e) => setMessageDraft(e.target.value)}
                    />
                </label>
                <button type="submit">Send</button>
            </form>
            <ul>
                {messages.map(({ username, content }, index) => {
                    return (<li key={index}>{`${username}: ${content}`}</li>)}
                )}
            </ul>
        </div>
    )
}

export default Chatpage;



// const requestOptions = {
//     method: 'PUT',
//     headers: { 'Content-Type': 'application/json' },
//     body: JSON.stringify(event)
// }
// const url = "http://localhost:8000/api/chatrooms/" + chatroomName;
// const response = await fetch(url, requestOptions)
// if (response.ok) {
//     console.log("we successfully added a message to the chatroom")
// }

// function connect(chatroom, chatroomName, user){
//     // const webscktURL = "ws://localhost:8000/ws/" + chatroomName + "/" + user;
//     // let websckt = null;
//     if (chatroom !== null && ws === null) {
//         let websckt = checkWebSocket(chatroomName, user);
//         console.log("inside connect", websckt)
//         websckt.onopen = () => {
//             websckt.send("Connected to react");
//             console.log("Connected");
//             console.log("Connected");
//         }
//         websckt.onmessage = (e) => {
//             const m = JSON.parse(e.data);
//             setMessages([...messages, m])
//         }
//         setMessages(chatroom.messages)
//         setWs(websckt)
//     }
// };
