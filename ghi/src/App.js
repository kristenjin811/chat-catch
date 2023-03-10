import React from 'react';
import Chat from './Chat'
import Login from './Login'
import Register from './Register'
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom"

import "./App.css"
import { AuthProvider, useToken } from './GetToken'


function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null
}

function App() {

  return (
    <BrowserRouter basename="/chat-catch/">
      <AuthProvider>
        <GetToken />
          <div className="container">
            <Routes>
              <Route path="/" element={<Login />} />
              <Route path="register/" element={<Register />} />
              <Route path="chats/" element={<Chat />} />
            </Routes>
          </div>
        </AuthProvider>
      </BrowserRouter>
  )
}


export default App
