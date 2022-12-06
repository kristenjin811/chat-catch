import {useState, useEffect} from 'react'
// import { useNavigate } from "react-router-dom";
// import Chat from "./CHT.js"

let ws = null;

function checkWebSocket(chatroomName, user) {
    if (ws === null || ws.readyState === WebSocket.CLOSED) {
        const socketURL = "ws://localhost:8000/ws/" + chatroomName + "/" + user;
        ws = new WebSocket(socketURL)
    }
    return ws
}



const Chatpage = () => {
    const [chatrooms, setChatrooms] = useState([]);
    const [selectedChatroom, setSelectedChatroom] = useState("ThroneRoom"); //what is the datatype?
    const [user, setUser] = useState("jared");
    const [chatroomName, setChatroomName] = useState("")


    const intializeChatroom = (selectedChatroom) => {
        setSelectedChatroom(selectedChatroom);
        setChatroomName(`${selectedChatroom}`)
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
                    onChange={(e) => intializeChatroom(e.target.value)}
                >
                    <option>{selectedChatroom}</option>
                    {chatrooms?.map(({_id, chatroom_name}) => {
                        return (
                        <option key={_id} value={chatroom_name}>
                            {chatroom_name}
                        </option>
                        );
                    })}
                </select>
                <label>User: <input type="text" id="user" autoComplete="off" defaultValue={user} onChange={(e) => setUser(e.target.value)}/></label>
                <button
                    // onClick={connect(ws, selectedChatroom, user)}
                >
                    Connect!
                </button>
            </div>
            <div>
            {/* <h1>Welcome to {selectedChatroom}!</h1> */}
            {/* <form onSubmit={addMessage}>
            <hr />
            <label>
                Message: <input type="text" id="messageText" autoComplete="off" defaultValue={message} onChange={(e) => setMessage(e.target.value)} />
            </label>
            <button
                type="submit"
            >Send</button>
            </form> */}
            <Messages {...{"s": selectedChatroom, "u": user}}/>
            </div>
        </div>
    );
}
// this component wants to connect to ws, fetch selectedChatroom.messages to render,
//and set logic for uploading messages
const Messages = (s,u) => {
    const [messages, setMessages] = useState([])
    const [message, setMessage] = useState("Hello")
    const [ws, setWs] = useState(null)
    const [chatroom, setChatroom] = useState(null)
    const chatroomName = s["s"]
    const user = s["u"]
    // console.log("user", user, typeof user)
    // console.log("line 88", typeof s, s)
    console.log("line 94 - logging message", user, message, chatroomName)
    // const addMessage = (event, user, message) => {
    //     event.preventDefault()
    //     ws.send({"username": user, "message": message})
    // }

    // useEffect(() => {
    // console.log("line 101 -- above addMessageApi", message, user, chatroomName)
    // async function addMessageAPI(user, message, chatroomName, event) {
    //     console.log("line 103 -- inside addMessageAPI", user, message, chatroomName)
    //     const requestOptions = {
    //         method: 'PUT',
    //         headers: { 'Content-Type': 'application/json' },
    //         body: JSON.stringify({"username": user, "message": message, "chatroom": chatroomName})
    //     }
    //     const url = "http://localhost:8000/api/chatrooms/" + chatroomName;
    //     // console.log(requestOptions.body)
    //     const response = await fetch(url, requestOptions)
    //     if (response.ok) {
    //         console.log("we successfully added a message to the chatroom")
    //     }
    //     event.preventDefault()
    // };
    //     addMessageAPI();
    // }, [message, user, chatroomName])

    useEffect(() => {
        const fetchSelectedChatroom = async () => {
            const url = "http://localhost:8000/api/chatrooms/" + chatroomName;
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                // console.log("Fetched Selected Chatroom as chatroom")
                setChatroom(data);
                // console.log("line 108 - data.messages", data.messages)
                setMessages(data.messages)
            }
        };
        fetchSelectedChatroom();
    }, [chatroomName])

    async function handleMessageSubmit(event, user, message, chatroomName){
        event.preventDefault()
        console.log("line 137 -- inside handleMessageSubmit", event, user, message, chatroomName)
        const requestOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({"username": user, "message": message, "chatroom": chatroomName})
        }
        console.log("request.body", requestOptions.body)
        const url = "http://localhost:8000/api/chatrooms/" + chatroomName;
        const response = await fetch(url, requestOptions)
        if (response.ok) {
            console.log("we successfully added a message to the chatroom")
        }
    }

    return (
        <div>
            <form onSubmit={handleMessageSubmit}>
                <hr />
                <label>
                    Message:
                    <input
                        type="text"
                        id="messageText"
                        autoComplete="off"
                        defaultValue={message}
                        onChange={(e) => setMessage(e.target.value)}
                    />
                </label>
                <button type="submit">Send</button>
            </form>
            <ul>
                {messages.map(({username, content, index}) => {
                    return (<li key={index}>{`${username}: ${content}`}</li>)}
                )}
            </ul>
        </div>
    )
}

export default Chatpage;



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
    // connect(chatroom, chatroomName, user);
 // useCallback(() => {
    //     const addMessage = async () => {
    //         if (selectedChatroom !== null) {
    //             const requestOptions = {
    //                 method: 'PUT',
    //                 headers: {'Content-Type': 'application/json'},
    //                 body: JSON.stringify({"username": user, "messages": message, "chatroom": selectedChatroom})
    //             }
    //             const url = `http://localhost:8000/api/chatrooms/${selectedChatroom}`
    //             fetch(url, requestOptions)
    //         };
    //         addMessage();
    //     };
    // }, [message, user, selectedChatroom]);

    // useEffect(function connect(ws, selectedChatroom, user){
    //         if (chatroom !== null && user !== null) {
    //             ws = new WebSocket(`ws://localhost:8000/ws/${selectedChatroom.chatroom_name}`);
    //         }
    //         connect();
    //     }, [selectedChatroom]);

    // useEffect(()=> {
    //     const sendMessage = (message) => {
    //         // ws.send(message)
    //         Chatpage.addMessage()
    //         setMessage('')
    //         sendMessage();
    //     };
    // }, [message]);
