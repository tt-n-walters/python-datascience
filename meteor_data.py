import sys
sys.path.append(sys.path.pop(0))

import csv
import collections

from meteor import Meteor
from map_value import map_value

# import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy


# Abstraction


def read_file(filename):
    # Open the meteorite data
    file = open(filename, "r", encoding="utf-8")
    data = file.read()
    file.close()

    # print(len(data))
    # print(type(data))

    # Split the data into 45,000 rows
    rows = data.splitlines()

    # Use CSV reader for more advanced data splitting
    csv_rows = list(csv.reader(rows))

    # print(len(rows))
    # print(type(rows))

    # Separate the column names from the data
    column_names = csv_rows.pop(0)

    return column_names, csv_rows


def process_meteorites(column_names, rows):
    for i in range(len(rows)):
        cells = rows[i]

        meteor = {}
        for i, column in enumerate(column_names):
            cell = cells[i]
            meteor[column] = cell

        try:
            # Data conversion attempt
            meteor_object = Meteor(**meteor)
        except ValueError:
            # Skip meteorite if any data missing
            continue
        
        yield meteor_object


# Call all our functions
column_names, rows = read_file("meteorites.csv")
meteorites = process_meteorites(column_names, rows)


# Find the meteorite with the greatest mass
# largest_found = meteorites[0]
# for meteor in meteorites:
#     if meteor[4] > largest_found[4]:
#         largest_found = meteor


def get_mass(meteorite):
    return meteorite.mass


def get_name_length(meteorite):
    return len(meteorite.name)


def get_year(meteorite):
    return meteorite.year



earliest = min(meteorites, key=get_year)
print(earliest)

# latest = max(meteorites, key=get_year)
# print(latest)

exit()

latitudes = [meteor.latitude for meteor in meteorites]
longitudes = [meteor.longitude for meteor in meteorites]
sizes = [map_value(meteor.mass, 0, 60000000, 10, 300) for meteor in meteorites]
colours = []
for meteor in meteorites:
    colour_value = map_value(meteor.year, 860, 2013, 0, 255*2)
    if colour_value < 256:
        colours.append((255, 0, colour_value))
    else:
        colours.append((colour_value - 256, 0, 255))

figure, axes = pyplot.subplots()

axes.scatter(longitudes, latitudes, s=sizes, alpha=0.5)

# Open an interactive window
# pyplot.show()

# Save the image to a file
# pyplot.savefig("output.png")
