// src/HomePage.js
import React, { useState } from 'react';
import ImageSlider from './ImageSlider'
import './HomePage.css'
function HomePage() {
  



  return (
    <div className = "container">
      <ImageSlider/>
      <h1 id = "aboutus_title">About our website</h1>
      <p>We are a passionate team dedicated to providing innovative solutions that make a difference in the world. 
        Our mission is to create high-quality products that solve real-world problems, and our vision is to continuously evolve and adapt to meet the needs of our customers.</p>
      <p>With a team of experts in various fields, we work collaboratively to bring cutting-edge technology and services to market. 
        We believe in the power of collaboration, creativity, and a relentless drive for excellence.</p>
    </div>
  );
}



export default HomePage;
