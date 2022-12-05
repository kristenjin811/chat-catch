import {useState, useEffect} from 'react'
// import { useNavigate } from "react-router-dom";
// import Chat from "./CHT.js"

//use this to set chatroom
//import CHT module to show
// 1. "Welcome to "selectedChatroom"!"
// 2. Username input
// 3.
// 3. message input


const Chatpage = () => {
    const [chatrooms, setChatrooms] = useState([]);
    const [selectedChatroom, setSelectedChatroom] = useState(null);
    const [user, setUser] = useState(null);


    const intializeChatroom = (selectedChatroom) => {
        setSelectedChatroom(selectedChatroom);
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
                    {chatrooms?.map((_id, chatroom_name) => {
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
            <Messages element={[selectedChatroom, user]}/>
            </div>
        </div>
    );
}
// this component wants to connect to ws, fetch selectedChatroom.messages to render,
//and set logic for uploading messages
const Messages = (selectedChatroom, user) => {
    const [messages, setMessages] = useState([])
    const [message, setMessage] = useState(null)
    const [ws, setWs] = useState(null)
    const [chatroom, setChatroom] = useState(null)
    console.log(selectedChatroom, user, chatroom)

    const addMessage = (event) => {
        event.preventDefault()
        ws.send({"username": user, message})
    }

    useEffect(() => {
        const fetchSelectedChatroom = async () => {
            const url = "http://localhost:8000/api/chatrooms" + selectedChatroom;
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                setChatroom(data);
            }
        };
        fetchSelectedChatroom();
    }, [selectedChatroom])

    function connect(chatroom){
            if (chatroom !== null && user !== null) {
                setWs(new WebSocket(`ws://localhost:8000/ws/${chatroom.chatroom_name}`));
                ws.onopen = () => {
                    ws.send("Connect");
                }
                ws.onmessage = (e) => {
                    const m = JSON.parse(e.data);
                    setMessages([...messages, m])
                }
                setMessages(chatroom.messages)
            }
        };

    return (
        <div>
            <form onSubmit={addMessage}>
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
                {messages.map(({user, message}) => {
                    return (<li>{`${user}: ${message}`}</li>)}
                )}
            </ul>
        </div>
    )
}

export default Chatpage;
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
