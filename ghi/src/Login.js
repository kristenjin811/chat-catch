import React, { useState } from 'react';
import './Login.css';
import {Link} from 'react-router-dom';


export default function Login(props) {
  const [email, setEmail] = useState('');
  const [pass, setPass] = useState('');

  const handleSubmit = (e) => {
      e.preventDefault();
      console.log(email);
  }

  return(
    <>
      <div className="window-wrapper">
        <p>Chat Catch</p>
        <div class="login-form">
          <form onSubmit={handleSubmit}>
            <label htmlFor="email">email</label>
            <input className="input" value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
            <label htmlFor="password">password</label>
            <input className="input" value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
            <button type="submit" className="btn btn-dark btn-block btn-large">Log In</button>
          </form>
          <Link className="register" to="register/">Register</Link>
        </div>
      </div>
    </>
  )
}
