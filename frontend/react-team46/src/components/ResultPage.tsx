import React from "react";
import "./ResultPage.css";

const ResultPage: React.FC = () => {
  const params = new URLSearchParams(window.location.search);
  const isAccepted = params.get("accepted") === "true";

  return (
    <div className="result-container">
      {isAccepted ? (
        <div className="result-card accepted">
          <h1>Congratulations!</h1>
          <p>Your application has been accepted. Welcome aboard!</p>
        </div>
      ) : (
        <div className="result-card rejected">
          <h1>We Regret to Inform You</h1>
          <p>
            Unfortunately, your application has not been accepted at this
            time. We encourage you to apply again in the future.
          </p>
          <button onClick={() => window.history.back()} className="back-button">
            Back to Status
          </button>
        </div>
      )}
    </div>
  );
};

export default ResultPage;
