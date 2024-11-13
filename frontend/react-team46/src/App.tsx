import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './components/Navbar';
import ImageSlider from './components/ImageSlider';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './components/HomePage';
import PetsPage from './components/PetsPage';
import LoginPage from './components/LoginPage';

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>
    <Navbar />
    <div className="app-content">
      {/* Other components and routes go here */}
      <Routes>
        <Route path="/" element={<HomePage/>} />
        <Route path="/pets" element={<PetsPage/>} />
        <Route path="/Login" element={<LoginPage/>} />
      </Routes>
    </div>
  </Router>
  )
}

export default App
