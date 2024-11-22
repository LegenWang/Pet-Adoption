import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./ApplicationDetailPage.css"; // Import the custom CSS

interface Application {
  id: number;
  user_name: string;
  user_age: number;
  user_occupation: string;
  user_salary: number;
  pet_name: string;
  pet_breed: string;
  status: string;
}

const ApplicationDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const [application, setApplication] = useState<Application | null>(null);

  useEffect(() => {
    async function fetchApplicationDetails() {
      try {
        const response = await fetch(`http://127.0.0.1:5000/applications/${id}`);
        const data = await response.json();
        setApplication(data);
      } catch (error) {
        console.error("Error fetching application details:", error);
      }
    }

    fetchApplicationDetails();
  }, [id]);

  const handleUpdateStatus = async (status: string) => {
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/applications/${id}/update_status`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ status }),
        }
      );
      const data = await response.json();
      setApplication(data.application);
    } catch (error) {
      console.error("Error updating application status:", error);
    }
  };

  if (!application) {
    return <p>Loading application details...</p>;
  }

  return (
    <div className="application-detail">
      <h1>Application Details</h1>
      <p>
        <strong>Applicant Name:</strong> {application.user_name}
      </p>
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
        <strong>Pet Name:</strong> {application.pet_name}
      </p>
      <p>
        <strong>Pet Breed:</strong> {application.pet_breed}
      </p>
      <p>
        <strong>Status:</strong> {application.status}
      </p>
      <div className="status-actions">
        <button onClick={() => handleUpdateStatus("Approved")}>Accept</button>
        <button onClick={() => window.history.back()} className="back-button">
            Back to Applications List
        </button>
        <button onClick={() => handleUpdateStatus("Rejected")}>Reject</button>
      </div>
    </div>
  );
};

export default ApplicationDetailPage;
