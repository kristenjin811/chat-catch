import logo from './chat-logo.png';
import './App.css';
// import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import ChatroomList from './websocket-test.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Where the world connects.
        </p>
        <a
          className="App-link"
          href="https://google.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          Where do you think this will take you?
        </a>
      </header>
    </div>
  );
}
// function App() {
//   return (
//     <BrowserRouter>
//         <Routes>
//             <Route path="chatrooms" element={<ChatroomList />} />
//         </Routes>
//     </BrowserRouter>
//   );
// }

export default App;
