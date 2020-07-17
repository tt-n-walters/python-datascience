
def map_value(value, minimum, maximum, lower, upper):
    value_position = (value - minimum) / (maximum - minimum)
    result = value_position * (upper - lower) + lower
    return result

# print(type(__name__))
# print(__name__)

if __name__ == "__main__":
    print(map_value(200, 0, 255, 0, 1))
    print(map_value(100, 0, 200, 1000, 1010))
