// import logo from './chat-logo.png';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import ChatroomList from './websocket-test.js';
// import UserList from './UserList';
// import Chat from './ChatRoom';
// import MessageForm from './messages';
import Chatpage from './WST'

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
        <Routes>
            {/* <Route path="users" element={<UserList /> } />
            <Route path="Chat" element={<Chat/>} /> */}
            {/* <Route path="Messages" element={<MessageForm /> } /> */}
            <Route path="chatrooms">
              <Route path="" element={<Chatpage /> } />
              {/* <Route path="string"  element={<Chat />} /> */}
            </Route>
        </Routes>
    </BrowserRouter>
  );
}

export default App;
