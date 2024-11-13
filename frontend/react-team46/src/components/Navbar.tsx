// src/components/Navbar.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Optional: for styling

const Navbar: React.FC = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/">Pet Adoption</Link>
      </div>
      <ul className="navbar-links">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/pets">Available Pets</Link>
        </li>
        <li>
          <Link to="/login">Login/Apply</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
