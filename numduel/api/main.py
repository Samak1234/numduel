import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "game"))

import random
import uuid
from fastapi import FastAPI, HTTPException
from api.models import StartGameRequest, GuessRequest
from difficulty import choose_difficulty
from hints import show_hint
from scoring import reducing_score

app = FastAPI()

games = {}

@app.get("/")
def root():
    return {"message": "NumDuel API is running"}

@app.post("/game/start")
def start_game(request: StartGameRequest):
    upper_limit, max_attempts, score = choose_difficulty(request.difficulty)

    if upper_limit is None:
        raise HTTPException(status_code=400, detail="Invalid difficulty. Choose easy, medium, or hard.")

    game_id = str(uuid.uuid4())

    games[game_id] = {
        "player_name": request.player_name,
        "difficulty": request.difficulty,
        "secret": random.randint(1, upper_limit),
        "upper_limit": upper_limit,
        "max_attempts": max_attempts,
        "score": score,
        "no_of_attempts": 0,
        "guesses": [],
        "hint_shown": False,
        "status": "active"
    }

    return {
        "game_id": game_id,
        "player_name": request.player_name,
        "difficulty": request.difficulty,
        "upper_limit": upper_limit,
        "max_attempts": max_attempts
    }