import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth0 } from "@auth0/auth0-react";

const Navbar: React.FC = () => {
  const navigate = useNavigate();
  const { logout, user } = useAuth0();

  const handleLogout = () => {
    logout({ 
      logoutParams: { 
        returnTo: window.location.origin 
      } 
    });
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-light container-fluid">
      <a className="navbar-brand" href="/">
        Pet Application
      </a>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item">
            <a className="nav-link" href="/pets">Pets</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/status">Status</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/application">Fill Application</a>
          </li>
        </ul>
        <div className="auth-info">
          <span>Welcome, {user?.name}</span>
          <button onClick={handleLogout} className="logout-btn">
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;