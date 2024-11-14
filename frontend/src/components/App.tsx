// src/App.tsx
import React from 'react';
import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import LoginPage from './LoginPage';
import ApplicationPage from './ApplicationPage';


function App() {
  const [count, setCount] = useState(0);

  return (
    <Router>
      
      <div className="app-content">
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/application" element={<ApplicationPage />} /> 
          <Route path="/" element={<Navigate to="/login" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;