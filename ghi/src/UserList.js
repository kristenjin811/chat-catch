import { useState, useEffect } from "react";

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      const url = "http://localhost:8000/api/users";
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setUsers(data);
      }
    };
    fetchUsers();
  }, []);

  return (
    <div className="container overflow-hidden mt-5">
      <select
        className="form-select"
        name="chatroom"
        id="chatroom"
        value=""
        onChange={(e) => setSelectedUser(e.target.value)}
      >
        <option value="">Choose a user</option>
        {users?.map(({ _id, username }) => {
          return (
            <option key={_id} value={username}>
              {username}
            </option>
          );
        })}
      </select>
    </div>
  );
};

export default UserList;
