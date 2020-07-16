import sys

sys.path.append(sys.path.pop(0))

from matplotlib import pyplot
import numpy as np
import math
import random

x_coords = np.arange(-10, 11, 0.2)
y_coords = [random.random() * 10 for x in x_coords]

sizes = [random.choice([10, 20, 50, 100, 200]) for x in x_coords]
all_colours = ["red", "orange", "blue", "green", "cyan", "purple"]
colours = [random.choice(all_colours) for x in x_coords]

pyplot.style.use("ggplot")

pyplot.scatter(x_coords, y_coords, s=sizes, c=colours, alpha=0.5)

pyplot.show()


# To save
# pyplot.savefig("output.png")
