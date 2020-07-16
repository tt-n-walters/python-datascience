
# class Direction:
#     north = 0
#     east = 1
#     south = 2
#     west = 3

# Direction.north


# class Restaurant:
#     occupancy = 20
#     staff = 8
#     seats_available = 15

#     def count_customers():
#         customers = Restaurant.occupancy - Restaurant.seats_available
#         print("There are currently", customers, "customers.")


# Restaurant.count_customers()
# Restaurant.seats_available -= 2
# Restaurant.count_customers()


class Restaurant:
    def __init__(self, name, oc, st, se):
        self.name = name
        self.occupancy = oc
        self.staff = st
        self.seats_available = se

    def count_customers(self):
        customers = self.occupancy - self.seats_available
        print("There are currently", customers, "customers.")

    def __add__(self, other):
        return Restaurant(
            "New Restaurant",
            self.occupancy + other.occupancy,
            self.staff + other.staff,
            self.seats_available + other.seats_available
        )

    def __repr__(self):
        return self.name + " with " + str(self.occupancy) + " tables and " + str(self.staff) + " employees."


burger_king = Restaurant("Burger King", 100, 30, 10)
kfc = Restaurant("KFC", 30, 8, 29)

# region burger_king.occupancy = 100
# burger_king.seats_available = 10

# kfc.occupancy = 30
# kfc.seats_available = 29

# burger_king.count_customers()
# kfc.count_customers()

# kfc.seats_available = 26

# burger_king.count_customers()


# print(hex(id(kfc.seats_available)))
# endregion print(hex(id(burger_king.seats_available)))

print(burger_king)
print(kfc)
print(burger_king + kfc)
