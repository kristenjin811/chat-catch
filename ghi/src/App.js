import React from 'react'
import Chat from './Chat'
import UserList from './UsersList'
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import "./App.css"

function App() {

  return (
     <BrowserRouter>
      <div className="container">
        <Routes>
          <Route path="/" element={<Chat />} />
          <Route path="users" element={<UserList />} />
        </Routes>
      </div>
    </BrowserRouter>

  )
}

export default App
