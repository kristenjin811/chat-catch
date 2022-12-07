import React, { useState } from 'react';
import './Register.css';
import {Link} from 'react-router-dom';


export default function Register(props) {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [name, setName] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }


  return(
    <>
      <div className="window-wrapper">
        <p>Chat Catch</p>
          <div className="form">
            <form className="register-form" onSubmit={handleSubmit}>
              <label htmlFor="name">full name</label>
              <input className="input" value={name} onChange={(e) => setName(e.target.value)} name="name" id="name" placeholder="full Name" />
              <label htmlFor="email">email</label>
              <input className="input" value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
              <label htmlFor="password">password</label>
              <input className="input" value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
              <button type="submit" className="btn btn-dark btn-block btn-large">Register</button>
            </form>
            <Link className="login" to="/">Login</Link>
          </div>
      </div>
    </>
  )
}
