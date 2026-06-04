import json
def save_score(attempts,player_name):

    score_data = {
        "attempts":attempts,
        "player_name":player_name
        }
    with open("../data/leaderboard.json","r") as file:

        data = json.load(file)

    data.append(score_data)

    with open("../data/leaderboard.json","w") as file:

        json.dump(data,file)
        
def show_leaderboard():

    with open("../data/leaderboard.json","r") as file:

        data = json.load(file)
         
    data.sort(key=lambda score: score["attempts"])

    print("\nLeaderboard: ")

    for index,score in enumerate(data,start=1):

        print(f"{index}. {score['player_name']} - {score['attempts']} attempts")