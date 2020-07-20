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

