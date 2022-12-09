import React, { useState } from 'react';
import './Login.css';
import {Link, useNavigate} from 'react-router-dom';
import { useToken } from "./GetToken";


export default function Login() {
  const [, login] = useToken();
  const [email, setEmail] = useState('');
  const [pass, setPass] = useState('');
  const [invalid, setInvalid] = useState(false);
  const navigate = useNavigate();

  const clearState = () => {
    setEmail("");
    setPass("");
    setInvalid("");
  };

  async function handleSubmit (e) {
    e.preventDefault();
    const error = await login(email, pass);
    if (error) {
      setInvalid(true);
    } else {
      clearState();
      navigate("chats/");
    }
  }

  return(
    <>
      <div className="window-wrapper">
        <p>Chat Catch</p>
        <div className="login-form">
          <form onSubmit={handleSubmit}>
            <label htmlFor="email">email</label>
            <input className="input" value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="youremail@gmail.com" id="email" name="email" />
            <label htmlFor="password">password</label>
            <input className="input" value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
            <button type="submit" className="btn btn-dark btn-block btn-large">Log In</button>
          </form>
          <Link className="register" to="register/">Register</Link>
          {invalid && (
            <div
              className="alert alert-danger mb-0 p-4 mt-4"
              id="invalid-message"
            >
              You've entered an incorrect email and/or password. Please
              try again.
            </div>
          )}
        </div>
      </div>
    </>
  )
}
