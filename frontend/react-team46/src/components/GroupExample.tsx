import React from 'react';
import Card from 'react-bootstrap/Card';
import CardGroup from 'react-bootstrap/CardGroup';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Link } from 'react-router-dom'; // Impor

const pets = [
  {
    "adopted": 0,
    "age": 4,
    "breed": "Golden Retreiver",
    "id": 1,
    "name": "Buddy"
  },
  {
    "adopted": 0,
    "age": 6,
    "breed": "Bulldog",
    "id": 2,
    "name": "Rex"
  },
  {
    "adopted": 0,
    "age": 8,
    "breed": "Mixed",
    "id": 3,
    "name": "Tucker"
  },
  {
    "adopted": 0,
    "age": 0,
    "breed": "TEST1",
    "id": 4,
    "name": "TESTNAME1FRONTEND"
  },
  {
    "adopted": 0,
    "age": 1,
    "breed": "TEST2",
    "id": 5,
    "name": "TESTNAME2FRONTEND"
  },
  {
    "adopted": 0,
    "age": 2,
    "breed": "TEST3",
    "id": 6,
    "name": "TESTNAME3FRONTEND"
  }
];

function GroupExample() {
  return (
    <Row>
      {pets.map((pet, index) => (
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
              {/* Link to the pet's details page */}
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
}

export default GroupExample;