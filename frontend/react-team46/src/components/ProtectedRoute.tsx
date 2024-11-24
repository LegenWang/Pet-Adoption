import React from "react";
import { Navigate } from "react-router-dom";

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const role = localStorage.getItem('role');

  // Debug: Log the role to check its value
  console.log("User Role: ", role);

  if (role !== 'manager') {
    // Redirect to a different page if not a manager
    return <Navigate to="/" />;
  }

  return <>{children}</>;
};

export default ProtectedRoute;
