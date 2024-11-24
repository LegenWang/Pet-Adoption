// src/HomePage.js
import React from "react";
import { useNavigate } from "react-router-dom";
import "./AppStatus.css";

const statusItems = [
  { label: "Received", checked: false },
  { label: "Under Review", checked: false },
  { label: "Additional Information Required", checked: false },
  { label: "In Progress", checked: false},
  {
    label: "Completed, click here to see the result",
    checked: true,
    isLink: true,
  },
];

const ApplicationStatus: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="container_app">
      <h1>Congratulations! You’ve successfully submitted the application.</h1>
      <p>Your application status is below:</p>

      <ul className="status-container">
        {statusItems.map((item, index) => (
          <li key={index} className="status-item">
            {item.isLink ? (
              <a
              href="/result?accepted=true"
              onClick={(e) => {
                e.preventDefault();
                navigate("/result?accepted=true");
              }}
            >
              {item.label}
            </a>
            ) : (
              <label htmlFor={`status-${index}`}>{item.label}</label>
            )}
            <input
              type="checkbox"
              id={`status-${index}`}
              checked={item.checked}
              readOnly
              disabled
            />
          </li>
        ))}
      </ul>

      <button onClick={() => navigate("/")}>Cancel application</button>
    </div>
  );
};

export default ApplicationStatus;
