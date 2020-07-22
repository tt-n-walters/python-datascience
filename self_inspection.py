# print(10 + 20)
# print(int(10).__add__(int(20)))
# print.__call__(int.__add__(int(10), int(20)))

# bob = { "name": "Bob", "last": "the Builder", "age": 42 }
# bob = object.__new__(dict).__init__(...)

# print("Hello world!")
# print.__call__(str("Hello world"))



class Car:
    max_speed = 100
    curr_speed = 0
    acceleration = 5

    def drive():
        Car.curr_speed += Car.acceleration
        if Car.curr_speed > Car.max_speed:
            Car.curr_speed = Car.max_speed
        print("Car currently driving at", Car.curr_speed, "kph")


Car.drive()
Car.drive()
Car.drive()
Car.drive()
Car.drive()
