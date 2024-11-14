// src/HomePage.js
import React, { useState } from 'react';
import './AppStatus.css';

const ApplicationStatus: React.FC = () => {
    return (
        <div className="container">
            <h1>Congratulations! You’ve successfully submitted the application.</h1>
            <p>Your application status is below:</p>
            
            <div className="status-container">
                <div className="status-item">
                    <label>Received</label>
                    <input type="checkbox" checked readOnly />
                </div>
                <div className="status-item">
                    <label>Under Review</label>
                    <input type="checkbox" checked readOnly />
                </div>
                <div className="status-item">
                    <label>Additional Information Required</label>
                    <input type="checkbox" checked readOnly />
                </div>
                <div className="status-item">
                    <label>In Progress</label>
                    <input type="checkbox" checked readOnly />
                </div>
                <div className="status-item">
                    <label>Completed, click here to see the result</label>
                    <input type="checkbox" checked readOnly />
                </div>
            </div>

            <button>Cancel application</button>
        </div>
    );
}


export default ApplicationStatus;
