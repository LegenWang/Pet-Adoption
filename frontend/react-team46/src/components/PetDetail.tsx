import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import "./PetDetail.css"; // Import the custom CSS

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: string;
  adopted: boolean;
}

const PetDetail = () => {
  const { id } = useParams(); // Extract the pet id from URL parameters
  const [pet, setPet] = useState<Pet | null>(null);

  useEffect(() => {
    async function fetchPetDetails() {
      if (id) {
        try {
          // Use the id from useParams to fetch pet details
          const response = await fetch(`http://127.0.0.1:5000/pets/${id}`);
          const data = await response.json();
          setPet(data);
        } catch (error) {
          console.error("Error fetching pet details:", error);
        }
      }
    }
    fetchPetDetails();
  }, [id]); // Fetch data whenever id changes

  if (!pet) return <div>Loading...</div>; // Loading state

  return (
    <div className="pet-detail-container">
      <h1>{pet.name}</h1>
      <img src={`../../public/images/pets/${pet.id}.jpg`} alt={pet.name} />
      <p>
        <strong>Breed:</strong> {pet.breed}
      </p>
      <p>
        <strong>Age:</strong> {pet.age}
      </p>
      <p className={pet.adopted ? "adopted-status" : "available-status"}>
        {pet.adopted
          ? "This pet is adopted"
          : "This pet is available for adoption"}
      </p>
      <Link to="/" className="back-button">
        Back to Pet List
      </Link>
    </div>
  );
};

export default PetDetail;