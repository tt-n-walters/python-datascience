import sys

sys.path.append(sys.path.pop(0))

# loc = sys.path.path(0)
# sys.path(loc)

from matplotlib import pyplot
import numpy as np
import math

# x_coords = range(-10, 11, 0.01)
# x_coords = [x / 100 for x in range(-10 * 100, 11 * 100)]
x_coords = np.arange(-10, 11, 0.2)

# def y(x):
# #     return (x ** 3) + 2 * (x ** 2) - x
#     return x * 0.5

# y_coords = list(map(y, x_coords))


y_coords = list(map(math.sin, x_coords))

pyplot.plot(x_coords, y_coords, "m-.")

pyplot.xlim(-10, 10)
pyplot.ylim(-3, 3)

pyplot.show()

# To save
# pyplot.savefig("output.png")

