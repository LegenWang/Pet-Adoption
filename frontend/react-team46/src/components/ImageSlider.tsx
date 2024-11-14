import React from "react";
import { Carousel } from "react-bootstrap"; // Make sure react-bootstrap is installed
import "./ImageSlider.css";

const BootstrapCarousel = () => {
  return (
    <Carousel>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src="./images/image1.jpg"
          alt="First slide"
        />
        <Carousel.Caption>
          <h3>Pet 1</h3>
          <p>Some description for pet 1.</p>
        </Carousel.Caption>
      </Carousel.Item>

      <Carousel.Item>
        <img
          className="d-block w-100"
          src="./images/image2.jpg"
          alt="Second slide"
        />
        <Carousel.Caption>
          <h3>PET 2</h3>
          <p>Some description for pet 2.</p>
        </Carousel.Caption>
      </Carousel.Item>

      <Carousel.Item>
        <img
          className="d-block w-100"
          src="./images/image3.jpg"
          alt="Third slide"
        />
        <Carousel.Caption>
          <h3>PET 3</h3>
          <p>Some description for pet 3.</p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
};

export default BootstrapCarousel;
