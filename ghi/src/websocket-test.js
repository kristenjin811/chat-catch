import {useState, useEffect} from 'react'

const ChatroomList = () => {
    const [chatrooms, setChatrooms] = useState([]);

    useEffect(() => {
        const fetchChatrooms = async () => {
            const url = "http://localhost:8081/db/chat_catch/chatrooms/";
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                setChatrooms(data.chatrooms);
            }
        };
        fetchChatrooms();
    }, []);

    return (
        <div className="container overflow-hidden mt-5">
            <select
                className="form-select"
                name="chatroom"
                id="chatroom"
                required
                defaultValue=""
                value={chatrooms}
                onChange={setChatrooms}
            >
                <option> Choose a chatroom </option>
                {chatrooms.map((chatroom) => {
                    return (
                    <option
                        key={chatroom.chatroom_name}
                        value={chatroom.chatroom_name}
                    >
                        {chatroom.chatroom_name}
                    </option>
                    )
                })}

            </select>
        </div>
    )
}

export default ChatroomList;
