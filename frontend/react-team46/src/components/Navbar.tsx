import React from "react";

import "./Navbar.css";

const Navbar: React.FC = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light container-fluid">
      <a className="navbar-brand" href="/">
        Pet Application
      </a>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item">
            <a className="nav-link" href="/pets">
              Pets
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/login">
              Login
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/status">
              Status
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/application">
              Fill application
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
