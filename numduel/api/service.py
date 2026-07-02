import random
import uuid

games = {}


def create_game(player_name, difficulty, upper_limit, max_attempts, score):
    game_id = str(uuid.uuid4())

    games[game_id] = {
        "player_name": player_name,
        "difficulty": difficulty,
        "secret": random.randint(1, upper_limit),
        "upper_limit": upper_limit,
        "max_attempts": max_attempts,
        "score": score,
        "no_of_attempts": 0,
        "guesses": [],
        "hint_shown": False,
        "status": "active"
    }

    return game_id