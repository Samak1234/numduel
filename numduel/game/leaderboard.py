import json
import os

# Build the path relative to this file's location
# so it works no matter where you run the script from
LEADERBOARD_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "data", "leaderboard.json"
)


def _load_data():
    """Load leaderboard from file. Returns empty list if file missing or broken."""
    try:
        with open(LEADERBOARD_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save_data(data):
    """Write leaderboard to file. Creates the data/ folder if it doesn't exist."""
    os.makedirs(os.path.dirname(LEADERBOARD_PATH), exist_ok=True)
    with open(LEADERBOARD_PATH, "w") as file:
        json.dump(data, file, indent=2)


def save_score(attempts, player_name, difficulty):
    data = _load_data()

    score_data = {
        "attempts": attempts,
        "player_name": player_name,
        "difficulty": difficulty
    }

    # Match on BOTH name AND difficulty
    # so easy and hard scores are tracked separately
    for score in data:
        if score["player_name"] == player_name and score["difficulty"] == difficulty:
            if attempts < score["attempts"]:
                score["attempts"] = attempts
            _save_data(data)  # save whether or not we updated
            return            # stop here, no need to append

    # Player not found for this difficulty — add new record
    data.append(score_data)
    _save_data(data)


def show_leaderboard():
    data = _load_data()

    if not data:
        print("No scores yet")
        return

    data.sort(key=lambda s: s["attempts"])

    print("\n🏆 Leaderboard")
    print("-" * 50)
    print(f"{'Rank':<5}| {'Player':<12}| {'Attempts':<9}| Difficulty")
    print("-" * 50)

    for index, score in enumerate(data, start=1):
        print(
            f"{index:<5}| "
            f"{score['player_name']:<12}| "
            f"{score['attempts']:<9}| "
            f"{score['difficulty']}"
        )
    print("-" * 50)