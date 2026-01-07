# Flask Superheroes API

A RESTful API for tracking heroes and their superpowers, built with Flask and SQLAlchemy.

## Author
Camila D

## Description
This API allows you to manage a database of superheroes, their powers, and the relationships between them. It provides endpoints to create, read, and update heroes, powers, and their associations. The API also includes email functionality for notifications.

## Features
- **Hero Management**: Retrieve all heroes or individual hero details with their powers
- **Power Management**: View all powers, get specific power details, and update power descriptions
- **Hero-Power Associations**: Create relationships between heroes and powers with strength ratings
- **Email Notifications**: Send emails through the API
- **Data Validation**: Ensures data integrity with model-level validations
- **RESTful Design**: Follows REST conventions for intuitive API usage

## Technologies Used
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Mail
- SQLAlchemy-Serializer
- SQLite

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd phase4--codechallenge
```

2. Create virtual environment and install dependencies:
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

3. Set up environment variables (optional for email functionality):
```bash
export MAIL_USERNAME=your-email@gmail.com
export MAIL_PASSWORD=your-app-password
```

4. Initialize the database:
```bash
venv/bin/python -m flask db init
venv/bin/python -m flask db migrate -m "Initial migration"
venv/bin/python -m flask db upgrade
```

5. Seed the database:
```bash
venv/bin/python seed.py
```

6. Run the application:
```bash
venv/bin/python app.py
```

The API will be available at `http://localhost:5555`

## API Endpoints

### Heroes

#### GET /heroes
Returns a list of all heroes.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  }
]
```

#### GET /heroes/:id
Returns details of a specific hero including their powers.

**Response (Success):**
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "hero_id": 1,
      "id": 1,
      "power": {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
      },
      "power_id": 2,
      "strength": "Strong"
    }
  ]
}
```

**Response (Not Found):**
```json
{
  "error": "Hero not found"
}
```

### Powers

#### GET /powers
Returns a list of all powers.

**Response:**
```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
]
```

#### GET /powers/:id
Returns details of a specific power.

**Response (Success):**
```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

**Response (Not Found):**
```json
{
  "error": "Power not found"
}
```

#### PATCH /powers/:id
Updates a power's description.

**Request Body:**
```json
{
  "description": "Valid Updated Description (at least 20 characters)"
}
```

**Response (Success):**
```json
{
  "id": 1,
  "name": "super strength",
  "description": "Valid Updated Description (at least 20 characters)"
}
```

**Response (Validation Error):**
```json
{
  "errors": ["Description must be at least 20 characters long"]
}
```

### Hero Powers

#### POST /hero_powers
Creates a new association between a hero and a power.

**Request Body:**
```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```

**Response (Success):**
```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
}
```

**Response (Validation Error):**
```json
{
  "errors": ["Strength must be 'Strong', 'Weak', or 'Average'"]
}
```

### Email

#### POST /send-email
Sends an email through the API.

**Request Body:**
```json
{
  "recipient": "recipient@example.com",
  "subject": "Test Subject",
  "body": "Email body content"
}
```

## Validations

### HeroPower
- `strength` must be one of: 'Strong', 'Weak', 'Average'

### Power
- `description` must be present and at least 20 characters long

## Database Schema

### Heroes
- id (Primary Key)
- name
- super_name

### Powers
- id (Primary Key)
- name
- description

### HeroPowers
- id (Primary Key)
- strength
- hero_id (Foreign Key)
- power_id (Foreign Key)

## Testing
Import the provided Postman collection to test all endpoints. The collection includes pre-configured requests for all API routes.

## Support
For issues or questions, please contact the repository owner.

## License
This project is licensed under the MIT License.
