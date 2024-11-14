import "./App.css";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import HomePage from "./components/HomePage";
import PetsPage from "./components/PetsPage";
import LoginPage from "./components/LoginPage";
import ApplicationPage from "./components/ApplicationPage";
import StatusPage from "./components/StatusPage";
import "./components/Navbar.css";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="app-content">
        {/* Other components and routes go here */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/pets" element={<PetsPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/status" element={<StatusPage />} />
          <Route path="/application" element={<ApplicationPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
