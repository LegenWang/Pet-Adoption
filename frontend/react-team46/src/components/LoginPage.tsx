import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./LoginPage.css";

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [email, setEmail] = useState<string>(""); 
  const [password, setPassword] = useState<string>("");
  const [isRegistering, setIsRegistering] = useState<boolean>(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const endpoint = isRegistering ? "/register" : "/login";
  
    // Prepare payload for API request
    const payload: any = {
      username,
      password,
    };
  
    if (isRegistering) {
      payload.email = email; // Add email only when registering
    }
  
    try {
      const response = await axios.post('http://localhost:5000/users' + endpoint, payload, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      alert(response.data.message);
  
      if (!isRegistering) {
        navigate("/pets"); 
      } else {
        setIsRegistering(false); // Switch to login form after successful registration
      }
    } catch (error: any) {
      alert(error.response?.data.error || "An error occurred");
    }
  };  

  const toggleForm = () => {
    setIsRegistering(!isRegistering);
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h2 className="login-title">{isRegistering ? "Register" : "Log In"}</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="form-input"
              placeholder="Enter your username"
            />
          </div>
          {isRegistering && (
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="form-input"
                placeholder="Enter your email"
              />
            </div>
          )}
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="form-input"
              placeholder="Enter your password"
            />
          </div>
          <button type="submit" className="btn">
            {isRegistering ? "Register" : "Sign In"}
          </button>
        </form>
        <div className="toggle">
          <p>
            {isRegistering ? "Already have an account? " : "Don't have an account? "}
            <button onClick={toggleForm}>
              {isRegistering ? "Login" : "Register"}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
