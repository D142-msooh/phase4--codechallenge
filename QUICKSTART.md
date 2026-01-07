# Quick Start Guide

## Setup (First Time)

1. Install dependencies:
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

2. Initialize database:
```bash
venv/bin/python -m flask db init
venv/bin/python -m flask db migrate -m "Initial migration"
venv/bin/python -m flask db upgrade
```

3. Seed database:
```bash
venv/bin/python seed.py
```

## Running the Application

```bash
./run.sh
```

Or manually:
```bash
venv/bin/python app.py
```

The API will be available at: http://localhost:5555

## Testing

Use the provided Postman collection or run:
```bash
venv/bin/python test_api.py
```

## API Endpoints

- GET /heroes - List all heroes
- GET /heroes/:id - Get hero details
- GET /powers - List all powers
- GET /powers/:id - Get power details
- PATCH /powers/:id - Update power description
- POST /hero_powers - Create hero-power association
- POST /send-email - Send email (requires email configuration)

## Email Configuration (Optional)

Set environment variables:
```bash
export MAIL_USERNAME=your-email@gmail.com
export MAIL_PASSWORD=your-app-password
```

Or copy .env.example to .env and configure.
