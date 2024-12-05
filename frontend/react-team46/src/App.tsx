import "./App.css";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import HomePage from "./components/HomePage";
import PetDetail from "./components/PetDetail";
import LoginPage from "./components/LoginPage";
import ApplicationPage from "./components/ApplicationPage";
import ApplicationStatus from "./components/AppStatus";
import ResultPage from "./components/ResultPage";
import "./components/Navbar.css";
import ApplicationViewPage from "./components/ApplicationViewPage";
import ApplicationDetailPage from "./components/ApplicationDetailPage";
import ProtectedRoute from "./components/ProtectedRoute";
import { useAuth0 } from "@auth0/auth0-react";

function App() {
  const { isAuthenticated, isLoading, user, loginWithRedirect } = useAuth0();

  // Handle loading state
  if (isLoading) {
    return <div>Loading...</div>;
  }

  // Redirect to login if not authenticated
  if (!isAuthenticated) {
    loginWithRedirect();
    return null;
  }

  return (
    <Router>
      <Navbar />

      <div className="app-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/pets" element={<PetDetail key="pets-list" />} />
          <Route path="/pets/:id" element={<PetDetail key="pet-detail" />} />
          <Route path="/status" element={<ApplicationStatus />} />
          <Route path="/application" element={<ApplicationPage />} />
          <Route path="/result" element={<ResultPage />} />

          {/* Protected Routes */}
          <Route
            path="/application-view"
            element={
              <ProtectedRoute>
                <ApplicationViewPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/applications/:id"
            element={
              <ProtectedRoute>
                <ApplicationDetailPage />
              </ProtectedRoute>
            }
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;