// src/HomePage.js
import React, { useState } from 'react';
import ImageSlider from './ImageSlider'
import './HomePage.css'
function HomePage() {
  



  return (
    <div className = "container">
      <div className = 'ImageInfo'>
      <ImageSlider/>
      </div>

      <div className = "aboutus">
        <h1 className = "aboutus_title">
          About Us
        </h1>
        <p1 className = 'aboutus_body'>
          
Welcome to Pet Adoption, the premier online pet adoption platform dedicated to connecting loving families with furry friends in need of a forever home. Our mission is to make the adoption process as simple, transparent, and joyful as possible. We understand that adopting a pet is a life-changing decision, and we’re here to support you every step of the way. From detailed pet profiles to advice on integrating your new companion into your family, our team is committed to providing you with all the resources you need to ensure a successful adoption experience.
        </p1>
        <br></br>
        <p1 className = 'aboutus_body'>
          
        At Pet Adoption, we believe every pet deserves a chance to find a loving home. That’s why we work closely with shelters, rescues, and foster organizations across the country to give animals of all ages and breeds a second chance at happiness. Whether you’re looking for a playful puppy, a loyal dog, or a cuddly cat, our platform allows you to browse profiles, read heartwarming adoption stories, and even connect directly with adoptive families. Together, we can make a difference—one tail wag at a time!
        </p1>

      </div>
    </div>
  );
}



export default HomePage;
