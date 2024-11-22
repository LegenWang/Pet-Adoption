import React from 'react';
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Link } from 'react-router-dom';
import './list.css'; // Ensure your CSS file is imported

const GroupExample = ({ pets }) => {
  return (
    <Row className="card-group-sm">
      {pets.map((pet) => (
        <Col key={pet.id} xs={12} sm={6} md={3}> {/* Change md={4} to md={3} for 4 cards per row */}
          <Card>
            <Card.Img variant="top" src={`http://127.0.0.1:5000/${pet.image_url}`} />
            <Card.Body>
              <Card.Title>{pet.name}</Card.Title>
              <Card.Text>
                Age: {pet.age} years<br />
                Breed: {pet.breed}<br />
                Adopted: {pet.adopted ? 'Yes' : 'No'}
              </Card.Text>
            </Card.Body>
            <Card.Footer>
              <small className="text-muted">
                <Link to={`/pets/${pet.id}`} style={{ textDecoration: 'none' }}>
                  View Pet Details
                </Link>
              </small>
            </Card.Footer>
          </Card>
        </Col>
      ))}
    </Row>
  );
};

export default GroupExample;