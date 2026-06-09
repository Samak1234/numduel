import json


def save_score(
    attempts,
    player_name,
    difficulty
):

    score_data = {
        "attempts": attempts,
        "player_name": player_name,
        "difficulty": difficulty
    }

    with open("../data/leaderboard.json", "r") as file:

        data = json.load(file)

    found_player = False

    for score in data:

        if score["player_name"] == player_name:

            found_player = True

            if attempts < score["attempts"]:

                score["attempts"] = attempts
                score["difficulty"] = difficulty

            break

    if found_player == False:
        data.append(score_data)

    with open("../data/leaderboard.json", "w") as file:

        json.dump(data, file)


def show_leaderboard():

    with open("../data/leaderboard.json", "r") as file:

        data = json.load(file)

    data.sort(key=lambda score: score["attempts"])

    if len(data) == 0:
        print("No scores yet")
        return

    print("\n🏆 Leaderboard")
    print("-" * 50)
    print("Rank | Player      | Attempts | Difficulty")
    print("-" * 50)

    for index, score in enumerate(data, start=1):

        print(
            f"{index:<4} | "
            f"{score['player_name']:<11} | "
            f"{score['attempts']:<8} | "
            f"{score['difficulty']}"
        )