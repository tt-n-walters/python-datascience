import timeit

def timer(function):
    def wrapper():
        start = timeit.default_timer()
        function()
        end = timeit.default_timer()
        print("Took", end - start, "seconds to run.")
    return wrapper


@timer
def slow_function():
    print("Starting the slow function.")
    for _ in range(10000000):
        pass
    print("I think it's finished.")
    return None


@timer
def get_user_name():
    return input("Enter your name: ")


get_user_name()
