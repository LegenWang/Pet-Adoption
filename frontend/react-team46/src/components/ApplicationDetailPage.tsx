import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
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
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchApplicationDetails() {
      try {
        const response = await fetch(`http://127.0.0.1:5000/applications/${id}`);
        const data = await response.json();
        setApplication(data);
      } catch (error) {
        console.error("Error fetching application details:", error);
        setError("Failed to load application details.");
      }
    }

    fetchApplicationDetails();
  }, [id]);

  const handleUpdateStatus = async (status: string) => {
    setLoading(true);
    setError(null);
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

      if (!response.ok) {
        throw new Error("Failed to update application status.");
      }

      const data = await response.json();
      setApplication(data.application);
    } catch (error) {
      console.error("Error updating application status:", error);
      setError("Failed to update application status.");
    } finally {
      setLoading(false);
    }
  };

  if (error) {
    return <p className="error">{error}</p>;
  }

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
        <button
          onClick={() => handleUpdateStatus("Approved")}
          disabled={loading}
        >
          Accept
        </button>
        <button
          onClick={() => navigate(-1)}
          className="back-button"
          disabled={loading}
        >
          Back to Applications List
        </button>
        <button
          onClick={() => handleUpdateStatus("Rejected")}
          disabled={loading}
        >
          Reject
        </button>
        <button
          onClick={() => handleUpdateStatus("Pending")}
          disabled={loading}
        >
          Reset to Pending
        </button>
      </div>
      {loading && <p className="loading-message">Updating status...</p>}
    </div>
  );
};

export default ApplicationDetailPage;
