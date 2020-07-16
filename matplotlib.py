import sys

sys.path.append(sys.path.pop(0))

from matplotlib import pyplot
import numpy as np
import math

x_coords = np.arange(-10, 11, 0.2)
y_coords = list(map(math.sin, x_coords))

pyplot.plot(x_coords, y_coords, "m-.")

pyplot.xlim(-10, 10)
pyplot.ylim(-3, 3)

pyplot.show()


# To save
# pyplot.savefig("output.png")
