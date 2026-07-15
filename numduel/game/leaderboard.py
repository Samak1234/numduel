import json
import os
import sys

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..")
)

from database import get_cursor

# Build the path relative to this file's location
# so it works no matter where you run the script from
LEADERBOARD_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "data", "leaderboard.json"
)


def _load_data():
    """Load leaderboard from PostgreSQL."""

    connection,cursor=get_cursor()

    cursor.execute("""
        SELECT attempts, player_name, difficulty
        FROM leaderboard
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return [
        {
            "attempts": row[0],
            "player_name": row[1],
            "difficulty": row[2]
        }
        for row in rows
    ]


def save_score(attempts, player_name, difficulty):
    connection, cursor = get_cursor()

    cursor.execute("""
        SELECT attempts
        FROM leaderboard
        WHERE player_name = %s
        AND difficulty = %s
    """, (player_name, difficulty))

    existing_score = cursor.fetchone()

    # Match on BOTH name AND difficulty
    # so easy and hard scores are tracked separately
    if existing_score:

        # Update only if the new score is better
        if attempts < existing_score[0]:
            cursor.execute("""
                UPDATE leaderboard
                SET attempts = %s
                WHERE player_name = %s
                AND difficulty = %s
            """, (attempts, player_name, difficulty))

    else:
        # Player not found for this difficulty — add new record
        cursor.execute("""
            INSERT INTO leaderboard (
                player_name,
                attempts,
                difficulty
            )
            VALUES (%s, %s, %s)
        """, (player_name, attempts, difficulty))

    connection.commit()

    cursor.close()
    connection.close()


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