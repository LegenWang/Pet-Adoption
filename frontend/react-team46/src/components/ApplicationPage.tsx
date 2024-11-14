import React, { useState } from "react";
import "./ApplicationPage.css";

interface PetAdoptionFormData {
  email: string;
  phoneNumber: string;
  address: string;
  age: number;
  occupation: string;
  salary: number;
  ownedPetsBefore: string;
  fencedYard: string;
  hoursAlone: string;
}

const ApplicationPage: React.FC = () => {
  const [formData, setFormData] = useState<PetAdoptionFormData>({
    email: "",
    phoneNumber: "",
    address: "",
    age: 0,
    occupation: "",
    salary: 0,
    ownedPetsBefore: "",
    fencedYard: "",
    hoursAlone: "",
  });

  const handleInputChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>,
  ) => {
    setFormData({
      ...formData,
      [e.target.id]: e.target.value,
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log(formData);
    // Logic to submit form data: For example, we can send this data to an API or save it in a database.
  };

  return (
    <div className="application-container">
      <div className="application-card">
        <h2 className="application-title">Pet Adoption Application</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              value={formData.email}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="phoneNumber">Phone Number</label>
            <input
              type="tel"
              id="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="address">Address</label>
            <input
              type="text"
              id="address"
              value={formData.address}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="age">Age</label>
            <input
              type="number"
              id="age"
              value={formData.age}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="occupation">Occupation</label>
            <input
              type="text"
              id="occupation"
              value={formData.occupation}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="salary">Salary</label>
            <input
              type="number"
              id="salary"
              value={formData.salary}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="ownedPetsBefore">Have you owned pets before?</label>
            <input
              type="text"
              id="ownedPetsBefore"
              value={formData.ownedPetsBefore}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="fencedYard">Do you have a fenced yard?</label>
            <input
              type="text"
              id="fencedYard"
              value={formData.fencedYard}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="hoursAlone">
              How many hours will the pet be alone?
            </label>
            <input
              type="text"
              id="hoursAlone"
              value={formData.hoursAlone}
              onChange={handleInputChange}
              className="form-input"
            />
          </div>

          <button type="submit" className="btn">
            Submit Application
          </button>
        </form>
      </div>
    </div>
  );
};

export default ApplicationPage;
