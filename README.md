# NumDuel 🎯

NumDuel is a backend engineering learning project that began as a Python CLI number guessing game and gradually evolved into a REST API using FastAPI.

The project focuses on learning backend fundamentals such as modular architecture, persistence, API development, separation of concerns, and software design.

---

## Features

### Gameplay

- Multiple difficulty levels
  - Easy (1–50)
  - Medium (1–100)
  - Hard (1–500)
- Random number generation
- Higher / Lower hints
- Even / Odd hints
- Divisibility hints
- Guess history tracking
- Scoring system
- Replay support
- Quit option during gameplay

### Leaderboard

- Persistent leaderboard using JSON
- Best score tracking per player
- Difficulty-specific score tracking
- Sorted leaderboard by attempts
- Empty leaderboard handling

### FastAPI Backend

- REST API using FastAPI
- Interactive Swagger UI documentation
- Start a new game endpoint
- Submit guesses through API
- Retrieve leaderboard through API
- Request validation using Pydantic
- In-memory game state management
- Service layer for game creation

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Health check |
| POST | `/game/start` | Start a new game |
| POST | `/game/guess` | Submit a guess |
| GET | `/leaderboard` | View leaderboard |

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

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
│   ├── difficulty.py
│   ├── hints.py
│   ├── validators.py
│   ├── scoring.py
│   ├── replay.py
│   └── leaderboard.py
│
├── data/
│   └── leaderboard.json
│
├── tests/
│
├── README.md
└── learning.md
```

---

## Architecture

The project is divided into two layers.

### API Layer

Responsible for handling HTTP requests and responses.

- FastAPI
- Endpoints
- Request validation
- JSON responses

### Game Layer

Responsible for the game's business logic.

- Difficulty selection
- Hint generation
- Validation
- Scoring
- Leaderboard
- Replay logic

The API reuses the existing game modules instead of duplicating logic.

---

## Leaderboard Design

Each leaderboard entry is stored as JSON.

```json
{
  "player_name": "Samak",
  "attempts": 4,
  "difficulty": "hard"
}
```

The leaderboard stores only the player's best score for each difficulty.

---

## Persistence

Leaderboard data is stored in:

```text
data/leaderboard.json
```

Game sessions are currently stored in memory while the API is running.

```text
games = {}
```

If the server stops, active games are lost. Persistent game storage will be added using PostgreSQL.

---

## Concepts Practiced

- Functions
- Modules
- Refactoring
- Separation of Concerns
- JSON
- File Handling
- Persistence
- Testing with pytest
- FastAPI
- HTTP Requests & Responses
- REST APIs
- Pydantic
- Swagger UI
- In-memory State
- Service Layer
- Software Architecture

---

## What I Learned

Through NumDuel I learned that backend development is much more than writing functions.

Some recurring questions during development were:

- Where should this logic live?
- Which module owns this responsibility?
- How should data flow through the application?
- What belongs in the API layer versus the game layer?
- What data should persist after the application stops?
- How should requests and responses be structured?

Key transitions during development:

```text
CLI
        ↓
Modular Architecture
        ↓
Testing with pytest
        ↓
FastAPI Backend
        ↓
REST APIs
        ↓
Service Layer
```

---

## Future Roadmap

- PostgreSQL Integration
- SQLAlchemy ORM
- Persistent Game Sessions
- User Authentication
- Docker
- Deployment
- Frontend Interface
