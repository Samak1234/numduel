# 🎯 NumDuel

A production-ready backend-powered number guessing game built with **Python**, **FastAPI**, and **PostgreSQL**, featuring a cloud-hosted database on **Neon** and deployed on **Render**.

NumDuel began as a modular Python CLI application and evolved into a RESTful backend API with persistent storage, cloud deployment, and interactive API documentation.

---

## 🚀 Live Demo

**API:** https://numduel.onrender.com

**Interactive API Docs (Swagger):**
https://numduel.onrender.com/docs

---

## ✨ Features

- 🎮 Number guessing game with multiple difficulty levels
- 🏆 Persistent leaderboard stored in PostgreSQL
- ⚡ REST API built with FastAPI
- ☁️ Cloud-hosted PostgreSQL database using Neon
- 🌐 Public deployment on Render
- 🧪 Unit tested game logic
- 📁 Modular project architecture
- 🔐 Environment variable configuration with python-dotenv
- 📖 Automatic OpenAPI / Swagger documentation

---

# 🏗️ Tech Stack

## Backend

- Python 3.12
- FastAPI
- PostgreSQL
- psycopg2
- python-dotenv

## Database

- PostgreSQL
- Neon

## Deployment

- Render

## Testing

- pytest

---

# 📂 Project Structure

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
│   ├── leaderboard.py
│   ├── replay.py
│   ├── scoring.py
│   └── validators.py
│
├── tests/
│
├── database.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/numduel.git
cd numduel
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432
```

---

# ▶️ Running the API

Start the development server:

```bash
uvicorn api.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Running Tests

Execute the test suite:

```bash
pytest
```

---

# 🗄️ Database

NumDuel uses PostgreSQL for persistent leaderboard storage.

The database is hosted on **Neon** and accessed securely using environment variables.

---

# ☁️ Deployment

Backend deployment:

- **Hosting:** Render
- **Database:** Neon PostgreSQL

Live API:

```
https://numduel.onrender.com
```

Interactive documentation:

```
https://numduel.onrender.com/docs
```

---

# 📈 Project Evolution

This project evolved through multiple stages:

- CLI number guessing game
- Modular project architecture
- Automated tests with pytest
- JSON leaderboard
- PostgreSQL migration
- FastAPI REST API
- Cloud database with Neon
- Environment variable configuration
- Cloud deployment on Render

---

# 📚 Skills Demonstrated

- Python application development
- REST API design
- FastAPI
- PostgreSQL integration
- SQL
- Environment configuration
- Cloud database integration
- API deployment
- Testing with pytest
- Modular software architecture
- Git & GitHub workflow

---

# 🚀 Future Improvements

- JWT authentication
- User accounts
- Docker support
- GitHub Actions CI/CD
- Redis caching
- Rate limiting
- API versioning
- Frontend web application

---

# 👨‍💻 Author

**Samak**

Backend Developer

GitHub:
https://github.com/YOUR_USERNAME