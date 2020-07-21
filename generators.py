
def eager_function(amount):
    numbers = []
    for i in range(amount):
        numbers.append(i)
    return numbers


def lazy_function(amount):
    for i in range(amount):
        yield i


numbers = eager_function(10)
print(numbers)

numbers = lazy_function(10)
number_iterator = iter(numbers)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
