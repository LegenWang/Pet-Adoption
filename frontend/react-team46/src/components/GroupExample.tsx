import React from 'react';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Link } from 'react-router-dom';

const GroupExample = ({ pets }) => {
  return (
    <Row>
      {pets.map((pet) => (
        <Col key={pet.id} xs={12} sm={6} md={4}>
          <Card>
            <Card.Img variant="top" src={`../../public/images/pets/${pet.id}.jpg`} />
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