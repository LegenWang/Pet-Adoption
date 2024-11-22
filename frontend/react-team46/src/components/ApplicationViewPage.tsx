import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./ApplicationViewPage.css"; // Import the custom CSS

interface Application {
  id: number;
  user_name: string;
  user_age: number;
  user_occupation: string;
  user_salary: number;
  pet_name: string;
  pet_breed: string;
}

const ApplicationViewPage = () => {
  const [applications, setApplications] = useState<Application[]>([]);

  useEffect(() => {
    async function fetchApplications() {
      try {
        const response = await fetch("http://127.0.0.1:5000/applications");
        const data = await response.json();
        setApplications(data);
      } catch (error) {
        console.error("Error fetching applications:", error);
      }
    }

    fetchApplications();
  }, []);

  return (
    <div className="application-list">
      <h1>Manage Applications</h1>
      {applications.length === 0 ? (
        <p>No applications available to review.</p>
      ) : (
        applications.map((application) => (
          <div key={application.id} className="application-details-card">
            <h3>{application.user_name}</h3>
            <p>
              <strong>Age:</strong> {application.user_age}
            </p>
            <p>
              <strong>Occupation:</strong> {application.user_occupation}
            </p>
            <p>
              <strong>Salary:</strong> ${application.user_salary}
            </p>
            <p>
              <strong>Pet:</strong> {application.pet_name} ({application.pet_breed})
            </p>
            <div className="application-actions">
              <Link to={`/applications/${application.id}`}>View Details</Link>
              {/* Add buttons for accept/reject if needed */}
            </div>
          </div>
        ))
      )}
    </div>
  );
};

export default ApplicationViewPage;
