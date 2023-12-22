import React, { useState } from 'react';

const Compo = (props) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: ""
  });

  const createUser = (e) => {
    e.preventDefault();
    const newUser = { username, email, password };
    console.log("Welcome", newUser);
    setUsername("");
    setEmail("");
    setPassword("");
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  return (
    <div>
      <form onSubmit={createUser}>
        <div>
          <label>Username: </label>
          <input
            type="text"
            name="username"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              handleInputChange(e);
            }}
          />
        </div>
        <div>
          <label>Email Address: </label>
          <input
            type="text"
            name="email"
            value={email}
            onChange={(e) => {
              setEmail(e.target.value);
              handleInputChange(e);
            }}
          />
        </div>
        <div>
          <label>Password: </label>
          <input
            type="text"
            name="password"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
              handleInputChange(e);
            }}
          />
        </div>
        <input type="submit" value="Create User" />
      </form>

      {/* Display real-time input below the form */}
      <div>
        <h2>Real-time Input:</h2>
        <p>Username: {formData.username}</p>
        <p>Email: {formData.email}</p>
        <p>Password: {formData.password}</p>
      </div>
    </div>
  );
};

export default Compo;
