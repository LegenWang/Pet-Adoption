import React from "react";
import { useNavigate } from "react-router-dom";
import "./LoginPage.css";
import { useAuth0 } from "@auth0/auth0-react";

const LoginPage: React.FC = () => {
  const { loginWithRedirect } = useAuth0();
  const navigate = useNavigate();

  const handleAuth0Login = async () => {
    await loginWithRedirect({
      appState: {
        returnTo: "/"
      }
    });
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h2 className="login-title">Log In</h2>
        <div className="auth0-login">
          <p>Log in using Auth0:</p>
          <button className="btn auth0-btn" onClick={handleAuth0Login}>
            Login with Auth0
          </button>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;