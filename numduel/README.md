# NumDuel 🎯

NumDuel is a number guessing game that evolved from a simple Python CLI project into a backend engineering learning project.

The project explores backend concepts such as modular design, persistence, REST APIs, service layers, and database integration using PostgreSQL.

---

# Features

## Gameplay

- Multiple difficulty levels:
  - Easy (1-50)
  - Medium (1-100)
  - Hard (1-500)
- Random number generation
- Higher / Lower hints
- Even / Odd hints
- Divisibility hints
- Guess history tracking
- Scoring system
- Replay support
- Quit option during gameplay

---

## Leaderboard

- Persistent leaderboard using PostgreSQL
- Best score tracking per player
- Difficulty-specific score tracking
- Sorted leaderboard by attempts
- Empty leaderboard handling

---

## FastAPI Backend

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check endpoint |
| POST | `/game/start` | Starts a new game |
| POST | `/game/guess` | Submit a guess |
| GET | `/leaderboard` | Returns leaderboard data |

---

## Project Structure

```text
numduel/
│
├── api/
│   ├── main.py
│   ├── models.py
│   └── service.py
│
├── game/
│   ├── main.py
│   ├── difficulty.py
│   ├── hints.py
│   ├── validators.py
│   ├── scoring.py
│   ├── replay.py
│   └── leaderboard.py
│
├── tests/
│
├── database.py
├── README.md
├── learning.md
└── .gitignore
```

---

# Architecture

The project follows a layered architecture.

## CLI Layer

Handles player interaction for the terminal version.

Files:

- `game/main.py`

---

## API Layer

Handles incoming HTTP requests and responses.

Files:

- `api/main.py`

Responsibilities:

- Route handling
- Request validation
- Response formatting
- HTTP error handling

---

## Service Layer

Contains business logic related to game creation and state management.

Files:

- `api/service.py`

Responsibilities:

- Create games
- Store active game state
- Generate game IDs
- Manage game lifecycle

---

## Database Layer

Handles communication with PostgreSQL.

Files:

- `database.py`
- `game/leaderboard.py`

Responsibilities:

- Open database connections
- Execute SQL queries
- Store leaderboard entries
- Retrieve leaderboard data

---

# PostgreSQL Schema

## Leaderboard Table

```sql
CREATE TABLE leaderboard (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(50),
    attempts INTEGER,
    difficulty VARCHAR(20)
);
```

---

# Technologies Used

## Backend

- Python
- FastAPI
- Uvicorn

## Database

- PostgreSQL
- psycopg2

## Testing

- Pytest

## Version Control

- Git
- GitHub

---

# Running the CLI Version

```bash
cd game
python main.py
```

---

# Running the API Version

Start the server:

```bash
python -m uvicorn api.main:app --reload
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Example API Workflow

## Start Game

```http
POST /game/start
```

Request:

```json
{
    "player_name": "Samak",
    "difficulty": "hard"
}
```

Response:

```json
{
    "game_id": "4f3e4a21-58d5-4d88-92b1-59d7d4f5a123",
    "player_name": "Samak",
    "difficulty": "hard",
    "upper_limit": 500,
    "max_attempts": 7
}
```

---

## Make Guess

```http
POST /game/guess
```

Request:

```json
{
    "game_id": "4f3e4a21-58d5-4d88-92b1-59d7d4f5a123",
    "guess": 250
}
```

---

## View Leaderboard

```http
GET /leaderboard
```

---

# Concepts Practiced

- Functions
- Modules
- Refactoring
- Separation of Concerns
- Service Layer Pattern
- REST APIs
- HTTP
- Request Validation
- Error Handling
- JSON Serialization
- PostgreSQL
- SQL
- Database Persistence
- Git Branching Strategy
- Software Architecture Thinking

---

# Development Journey

The project evolved through several stages:

```text
Single File CLI
        ↓
Modular Architecture
        ↓
Persistent JSON Leaderboard
        ↓
FastAPI Backend
        ↓
Service Layer
        ↓
PostgreSQL Integration
```

---

# What I Learned

Building NumDuel taught me that backend development involves much more than writing code.

Some of the questions that repeatedly appeared during development were:

- Where should this logic live?
- Which module owns this responsibility?
- How should data flow through the application?
- Should this data be persisted?
- Should this functionality belong to the API layer or service layer?
- When should a database be introduced?

The project became an exercise in architecture and design decisions rather than simply implementing features.

---

# Future Improvements

- SQLAlchemy ORM integration
- Persistent game sessions
- Authentication and users
- Docker support
- Deployment
- Frontend client

---

# Author

Built by Samak as part of a backend engineering learning journey.