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
              pets
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/login">
              login
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/status">
              status
            </a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="/application">
              status
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
