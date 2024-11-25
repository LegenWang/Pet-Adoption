import React, { useEffect, useState } from "react";
import { Carousel } from "react-bootstrap"; // Ensure react-bootstrap is installed
import "./ImageSlider.css";

interface Pet {
  id: number;
  name: string;
  breed: string;
  age: number;
  adopted: boolean;
  image_url: string; // Include image_url to store image URL from the backend
}

const BootstrapCarousel = () => {
  const [pets, setPets] = useState<Pet[]>([]); // State to store pet data

  useEffect(() => {
    async function fetchPets() {
      try {
        const response = await fetch("http://127.0.0.1:5000/pets"); // Replace with your API URL
        const data = await response.json();
        // Shuffle pets array and limit to 6 pets
        const shuffledPets = data.sort(() => Math.random() - 0.5).slice(0, 6);
        setPets(shuffledPets);
      } catch (error) {
        console.error("Error fetching pets data:", error);
      }
    }

    fetchPets();
  }, []); // Fetch pets on component mount

  return (
    <Carousel>
      {pets.map((pet) => (
        <Carousel.Item key={pet.id}>
          <img
            className="d-block w-100"
            src={`http://127.0.0.1:5000/static/images/pets/${pet.id}.jpg`} // Use the image_url from API response
            alt={`Slide of ${pet.name}`}
          />
          <Carousel.Caption>
            <h3>{pet.name}</h3>
            <p>
              Breed: {pet.breed} | Age: {pet.age} years |{" "}
              {pet.adopted ? "Adopted" : "Available"}
            </p>
          </Carousel.Caption>
        </Carousel.Item>
      ))}
    </Carousel>
  );
};

export default BootstrapCarousel;