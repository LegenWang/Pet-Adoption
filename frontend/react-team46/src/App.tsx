import "./App.css";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import HomePage from "./components/HomePage";
import PetDetail from "./components/PetDetail";
import LoginPage from "./components/LoginPage";
import ApplicationPage from "./components/ApplicationPage";
import ApplicationStatus from "./components/AppStatus";
import "./components/Navbar.css";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="app-content">
        {/* Other components and routes go here */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/pets" element={<PetDetail />} />
          <Route path="/pets/:id" element={<PetDetail />} />

          <Route path="/login" element={<LoginPage />} />
          <Route path="/status" element={<ApplicationStatus />} />
          <Route path="/application" element={<ApplicationPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
