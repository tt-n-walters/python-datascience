# print(10 + 20)
# print(int(10).__add__(int(20)))
# print.__call__(int.__add__(int(10), int(20)))

# bob = { "name": "Bob", "last": "the Builder", "age": 42 }
# bob = object.__new__(dict).__init__(...)

# print("Hello world!")
# print.__call__(str("Hello world"))

print(bob.name)
print.__call__(Person.__getattribute__(bob, "name"))


class Car:
    def create_new(acceleration=5):
        max_speed = 100
        curr_speed = 0
        acceleration = acceleration
        return max_speed, curr_speed, acceleration

    def drive(car_info):
        car_info.curr_speed += car_info.acceleration
        if car_info.curr_speed > car_info.max_speed:
            car_info.curr_speed = car_info.max_speed
        print("Car currently driving at", car_info.curr_speed, "kph")


toyota = Car.create_new()

toyota = Car.drive(toyota)
toyota = Car.drive(toyota)
toyota = Car.drive(toyota)

# toyota.drive()
# Car.drive(toyota)

ferrari = Car.create_new(15)

ferrari = Car.drive(ferrari)
ferrari = Car.drive(ferrari)
ferrari = Car.drive(ferrari)
ferrari = Car.drive(ferrari)
ferrari = Car.drive(ferrari)