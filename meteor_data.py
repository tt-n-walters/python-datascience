import csv
import collections

from meteor import Meteor

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
    # Instantiate a new list to save every meteorite
    meteorites = []

    for i in range(len(rows)):
        # cells = rows[i].split(",")
        cells = rows[i]

        if cells[4]:
            # Convert 5th column "mass" to a float
            cells[4] = float(cells[4])
        else:
            # Otherwise skip to the next meteorite
            continue

        # region meteor = {
        #     "name": cells[0],
        #     "id": cells[1],
        #     "nametype": cells[2],
        #     "recclass": cells[3],
        #     "mass (g)": cells[4],
        #     "fall": cells[5],
        #     "year": cells[6],
        #     "reclat": cells[7],
        #     "reclong": cells[8],
        #     "GeoLocation": cells[9]
        # endregion }

        meteor = {}
        for i, column in enumerate(column_names):
            cell = cells[i]
            meteor[column] = cell

        meteor_object = Meteor(**meteor)

        meteorites.append(meteor_object)

    return meteorites


# Call all our functions
column_names, rows = read_file("meteorites.csv")
meteorites = process_meteorites(column_names, rows)

print(len(rows))
print(len(meteorites))

# Find the meteorite with the greatest mass
# largest_found = meteorites[0]
# for meteor in meteorites:
#     if meteor[4] > largest_found[4]:
#         largest_found = meteor


def get_mass(meteorite):
    return meteorite["mass (g)"]


def get_name_length(meteorite):
    return len(meteorite["name"])


largest = max(meteorites, key=get_name_length)

print(largest)


# Categorise by mass
boundaries = [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 50, 60, 70, 80, 90, 100, 200, 400, 800, 1600, 3200, 6400, 10000, 20000, 40000, 100000, 500000, 1000000, 2000000, 10000000, 20000000, 100000000]

meteors_by_mass = collections.defaultdict(int)

for meteor in meteorites:
    # Find the first boundary that the meteor has less mass than
    for bound in boundaries:
        if meteor.mass < bound:
            # Add one to that counter, and move to the next meteorite
            meteors_by_mass[bound] += 1
            break
    
print(meteors_by_mass)
print(sum(meteors_by_mass.values()))

# Sorting the meteor mass data
masses = meteors_by_mass.items()
sorted_masses = sorted(masses)

# x_values = list(meteors_by_mass.keys())
# y_values = list(meteors_by_mass.values())

bounds = [mass[0] for mass in sorted_masses]
counts = [mass[1] for mass in sorted_masses]
pyplot.pie(counts, labels=bounds, explode=numpy.linspace(0, 0.4, len(bounds)))

# Open an interactive window
pyplot.show()

# Save the image to a file
# pyplot.savefig("output.png")
