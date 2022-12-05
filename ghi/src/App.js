import React from 'react'
import Chat from './Chat'
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
        </Routes>
      </div>
    </BrowserRouter>

  )
}

export default App
