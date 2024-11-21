import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginPage.css";

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false); 
  const [isRegistering, setIsRegistering] = useState<boolean>(false); // Track if user is in register mode
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (isRegistering) {
      // Register user (basic simulation)
      alert(`Account created for ${username}! Please log in.`);
      setIsRegistering(false); // Switch back to login mode
    } else {
      if (!isLoggedIn) {
        // Log in user
        setIsLoggedIn(true);
        alert(`Welcome, ${username}! You are now logged in.`);
        navigate("/application");
      } else {
        alert("You are already logged in!");
      }
    }
  };

  const toggleForm = () => {
    setIsRegistering(!isRegistering); // Toggle between login and register form
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

          {/* Register specific field (optional email) */}
          {isRegistering && (
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                className="form-input"
                placeholder="Enter your email"
              />
            </div>
          )}

          <button type="submit" className="btn">
            {isRegistering ? "Register" : "Sign In"}
          </button>
        </form>

        {/* Toggle between login and register */}
        <div className="toggle">
          <p>
            {isRegistering
              ? "Already have an account? "
              : "Don't have an account? "}
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
