import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import "./PetDetail.css"; // Import the custom CSS
import GroupExample from "./GroupExample";

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
  const [pets, setPets] = useState<Pet[]>([]); // State for all pets

  useEffect(() => {
    async function fetchPetDetails() {
      if (id) {
        try {
          const response = await fetch(`http://127.0.0.1:5000/pets/${id}`);
          const data = await response.json();
          setPet(data);
        } catch (error) {
          console.error("Error fetching pet details:", error);
        }
      }
    }

    async function fetchAllPets() {
      try {
        const response = await fetch(`http://127.0.0.1:5000/pets`);
        const data = await response.json();
        setPets(data);
      } catch (error) {
        console.error("Error fetching pets:", error);
      }
    }

    fetchPetDetails();
    fetchAllPets();
  }, [id]); // Fetch data whenever id changes

  if (!pet) {
    return (
      <div>
        <GroupExample pets={pets} /> {/* Pass pets data */}
      </div>
    );
  }

  return (
    <div className="pet-detail-container">
      <h1>{pet.name}</h1>
      <img src={`http://127.0.0.1:5000/${pet.image_url}`} alt={pet.name} />
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