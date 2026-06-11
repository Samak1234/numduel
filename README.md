# NumDuel 🎯

NumDuel is a Python CLI number guessing game built as a backend engineering learning project.

What started as a simple guessing game gradually evolved into a modular application focused on software engineering concepts such as persistence, separation of concerns, data modeling, and architecture thinking.

---

## Features

### Gameplay

* Multiple difficulty levels

  * Easy (1-50)
  * Medium (1-100)
  * Hard (1-500)
* Random number generation
* Higher / Lower hints
* Even / Odd hints
* Divisibility hints
* Guess history tracking
* Scoring system
* Replay support
* Quit option during gameplay

### Leaderboard

* Persistent leaderboard using JSON
* Best score tracking per player
* Difficulty-specific score tracking
* Sorted leaderboard by attempts
* Empty leaderboard handling
* Improved leaderboard display

---

## Project Structure

```text
numduel/
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
├── data/
│   └── leaderboard.json
│
├── learning.md
└── README.md
```

---

## Architecture

The project follows a modular architecture where each module owns a single responsibility.

### main.py

Game orchestration and user interaction.

### difficulty.py

Difficulty configuration and game limits.

### hints.py

Hint generation logic.

### validators.py

Input validation.

### scoring.py

Score calculation and penalties.

### replay.py

Replay handling.

### leaderboard.py

Leaderboard persistence, sorting, and display.

---

## Leaderboard Design

Each leaderboard entry is stored as structured JSON:

```json
{
  "player_name": "samak",
  "attempts": 4,
  "difficulty": "hard"
}
```

The leaderboard stores only the best score for a player on a specific difficulty level.

---

## Persistence

Scores are persisted in:

```text
data/leaderboard.json
```

This allows leaderboard data to survive after the program exits.

Without persistence:

```text
Program closes → Data lost
```

With persistence:

```text
Program closes → Data remains
```

---

## Concepts Practiced

* Functions
* Modules
* Refactoring
* Separation of Concerns
* Data Modeling
* JSON Serialization / Deserialization
* File Handling
* Persistence
* Error Handling
* Structured Data
* Software Architecture Thinking

---

## What I Learned

Building NumDuel taught me that software development is not only about writing code.

Some of the questions I repeatedly faced were:

* Where should this logic live?
* Which module owns this responsibility?
* How should data flow through the application?
* How should leaderboard data be structured?
* Should this data be persisted?
* Should this functionality be displayed here or elsewhere?

Key transitions during development:

```text
Monolithic → Modular Architecture
Functions → Modules
Runtime State → Persistence
Data → Structured Data
JSON → Serialization / Deserialization
Single File → Separation of Concerns
Code Writing → Refactoring
Feature Building → Architecture Thinking
```

---

## Future Roadmap

* OOP Refactor
* FastAPI Backend
* PostgreSQL Integration
* REST API Endpoints
* Deployment
* Web Interface

##
