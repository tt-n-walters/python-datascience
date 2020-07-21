import datetime

import pandas as pd


def timestamp_converter(string):
    timestamp = int(float(string) / 1000)
    return datetime.datetime.fromtimestamp(timestamp)

converter_functions = {
    "created_at": timestamp_converter,
    "last_move_at": timestamp_converter
}
games = pd.read_csv("games.csv", converters=converter_functions)

# print(games.created_at[0])

date_point = datetime.datetime(year=2017, month=3, day=1)
games_after_2018 = games[games.created_at < date_point]


# Create a list of all unique player names
#   Iterate over all player names in the white_id and black_id columns,
#   if the name has not been found before, add to the list of names.
#   BONUS: Might look into the set() data structure
player_names = []
for name in games.white_id:
    player_names.append(name)

for name in games.black_id:
    player_names.append(name)

player_names = list(set(player_names))

print("Finished list of unique names.")

# Count wins for each player
#   Iterate over all unique player names, for each name count the number of wins
#   in the dataframe. eg. len(games[games.white_id == name][games.winner == "white"])
player_games = {}
for i, name in enumerate(player_names):
    if i % 10 == 0:
        print("Processed", i, "players.", end="\r")

    # Extract all the games played in
    games_as_white = games[games.white_id == name]
    games_as_black = games[games.black_id == name]
    won_white = games_as_white[games.winner == "white"]
    won_black = games_as_black[games.winner == "black"]

    count_won = len(won_white) + len(won_black)
    player_games[name] = count_won

print("Finished counting player wins.")

# Find the most successful player
#   If a dictionary is chosen to represent the number of wins for each player, then
#   max() can be used with a key-function to find the most successful player.

def get_player_wins(name):
    return player_games[name]

winner = max(player_games, key=get_player_wins)
print(winner, get_player_wins(winner))
