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
from validators import is_valid_guess
from leaderboard import save_score

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


@app.post("/game/guess")
def make_guess(request: GuessRequest):
    game = games.get(request.game_id)

    if not game:
        raise HTTPException(status_code=404, detail="Game not found.")

    if game["status"] != "active":
        raise HTTPException(status_code=400, detail=f"Game is already {game['status']}.")

    if not is_valid_guess(request.guess, game["upper_limit"]):
        raise HTTPException(status_code=400, detail=f"Guess must be between 1 and {game['upper_limit']}.")

    game["no_of_attempts"] += 1
    game["guesses"].append(request.guess)

    hint_shown, hints = show_hint(
        game["secret"],
        game["no_of_attempts"],
        game["max_attempts"],
        game["hint_shown"]
    )
    game["hint_shown"] = hint_shown

    if request.guess == game["secret"]:
        game["status"] = "won"
        save_score(game["no_of_attempts"], game["player_name"], game["difficulty"])
        return {
            "result": "correct",
            "attempts": game["no_of_attempts"],
            "score": game["score"],
            "hints": hints,
            "guesses": game["guesses"]
        }

    if game["no_of_attempts"] >= game["max_attempts"]:
        game["status"] = "lost"
        return {
            "result": "lost",
            "secret": game["secret"],
            "attempts": game["no_of_attempts"],
            "guesses": game["guesses"]
        }

    game["score"] = reducing_score(game["score"])

    return {
        "result": "too_high" if request.guess > game["secret"] else "too_low",
        "attempts_used": game["no_of_attempts"],
        "attempts_remaining": game["max_attempts"] - game["no_of_attempts"],
        "score": game["score"],
        "hints": hints,
        "guesses": game["guesses"]
    }


@app.get("/leaderboard")
def get_leaderboard():
    from leaderboard import _load_data
    data = _load_data()

    if not data:
        return {"leaderboard": []}

    data.sort(key=lambda s: s["attempts"])

    return {"leaderboard": data}