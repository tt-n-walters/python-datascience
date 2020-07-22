# print(10 + 20)
# print(int(10).__add__(int(20)))
# print.__call__(int.__add__(int(10), int(20)))

# bob = { "name": "Bob", "last": "the Builder", "age": 42 }
# bob = object.__new__(dict).__init__(...)

# print("Hello world!")
# print.__call__(str("Hello world"))

# print(bob.name)
# print.__call__(Person.__getattribute__(bob, "name"))


class Car:
    def __init__(self, acceleration=5):
        self.max_speed = 100
        self.curr_speed = 0
        self.acceleration = acceleration

    def drive(self):
        self.curr_speed += self.acceleration
        if self.curr_speed > self.max_speed:
            self.curr_speed = self.max_speed
        print("Car currently driving at", self.curr_speed, "kph")


toyota = Car(5)

toyota = object.__new__(Car)
Car.__init__(toyota, 5)


toyota.drive()

toyota = Car.drive(toyota)
