import React, { useState } from 'react';
import Chat from './Chat'
import UserList from './UsersList'
import Login from './Login'
import Register from './Register'
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
          <Route path="/" element={<Login />} />
          <Route path="register/" element={<Register />} />
          <Route path="chats/" element={<Chat />} />
          <Route path="users" element={<UserList />} />
        </Routes>
      </div>
    </BrowserRouter>

  )
}

export default App
