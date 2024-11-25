import React from "react";
import { useNavigate } from "react-router-dom";

const Navbar: React.FC = () => {
  const role = localStorage.getItem('role');
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('role');
    navigate("/login");
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
            <a className="nav-link" href="/login">Login</a>
          </li>
          {role === 'manager' && (
            <li className="nav-item">
              <a className="nav-link" href="/application-view">Manage Applications</a>
            </li>
          )}
          <li className="nav-item">
            <a className="nav-link" href="/status">Status</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/application">Fill Application</a>
          </li>
        </ul>
        <button onClick={handleLogout} className="logout-btn">
          Logout
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
