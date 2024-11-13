import React, { useState } from 'react';
import './ImageSlider.css';

// Image data (URL and respective link)
const images = [
  { src: '/images/image1.jpg', link: 'page1.html', alt: 'Image 1' },
  { src: '/images/image2.jpg', link: 'page2.html', alt: 'Image 2' },
  { src: '/images/image3.jpg', link: 'page3.html', alt: 'Image 3' },
  // Add more images as needed
];

const ImageSlider = () => {
  const [currentIndex, setCurrentIndex] = useState(0);

  // Handle next and previous button clicks
  const goToNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
  };

  const goToPrevious = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + images.length) % images.length);
  };

  return (
    <div className="image-slider">
      <div className="slider-item">
        <a href={images[currentIndex].link}>
          <img src={images[currentIndex].src} alt={images[currentIndex].alt} />
        </a>
      </div>

      {/* Arrow buttons */}
      <div className="slider-controls">
        <button onClick={goToPrevious} className="arrow-button left-arrow">←</button>
        <button onClick={goToNext} className="arrow-button right-arrow">→</button>
      </div>
    </div>
  );
};

export default ImageSlider;
