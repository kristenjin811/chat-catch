import React from 'react';
import Chat from './Chat'
// import UserList from './UsersList'
import Login from './Login'
import Register from './Register'
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import "./App.css"

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Where the world connects.
//         </p>
//         <a
//           className="App-link"
//           href="https://google.com"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Where do you think this will take you?
//         </a>
//       </header>
//     </div>
//   );
// }
function App() {

  return (
     <BrowserRouter>
      <div className="container">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="register/" element={<Register />} />
          <Route path="chats/" element={<Chat />} />
          {/* <Route path="users" element={<UserList />} /> */}
        </Routes>
      </div>
    </BrowserRouter>

  )
}

export default App
