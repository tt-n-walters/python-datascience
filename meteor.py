class Meteor:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.id = int(kwargs["id"])
        self.mass = float(kwargs["mass (g)"])
        self.fall = kwargs["fall"]
        self.year = int(kwargs["year"][6:10])
        self.latitude = float(kwargs["reclat"])
        self.longitude = float(kwargs["reclong"])

        if self.year > 2020:
            raise ValueError


    def get_location(self):
        pass


    def __repr__(self):
        return self.name + ", " + str(self.id) + ", " + str(self.mass) + ", " + str(self.year)