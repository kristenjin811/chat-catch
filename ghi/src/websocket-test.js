import {useState, useEffect} from 'react'

const ChatroomList = () => {
    const [chatrooms, setChatrooms] = useState([]);
    const [selectedChatroom, setSelectedChatroom] = useState(null);

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
      <div className="container overflow-hidden mt-5">
        <select
          className="form-select"
          name="chatroom"
          id="chatroom"
          value=""
          onChange={(e) => setSelectedChatroom(e.target.value)}
        >
          <option value="">Choose a chatroom</option>
          {chatrooms?.map(({ _id, chatroom_name }) => {
            return (
              <option key={_id} value={chatroom_name}>
                {chatroom_name}
              </option>
            );
          })}
        </select>

      </div>
    );
}

// const UserList = () => {
//   const [users, setUsers] = useState([]);
//   const [selectedUser, setSelectedUser] = useState(null);

//   useEffect(() => {
//     const fetchUsers = async () => {
//       const url = "http://localhost:8000/api/user";
//       const response = await fetch(url);
//       if (response.ok) {
//         const data = await response.json();
//         setUsers(data);
//       }
//     };
//     fetchUser();
//   }, []);

//   return (
//     <div className="container overflow-hidden mt-5">
//       <select
//         className="form-select"
//         name="chatroom"
//         id="chatroom"
//         value=""
//         onChange={(e) => setSelectedUser(e.target.value)}
//       >
//         <option value="">Choose a chatroom</option>
//         {users?.map(({ _id, user_name }) => {
//           return (
//             <option key={_id} value={user_name}>
//               {user_name}
//             </option>
//           );
//         })}
//       </select>
//     </div>
//   );
// };

export default ChatroomList;
