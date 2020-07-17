class Meteor:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.id = int(kwargs["id"])
        self.mass = float(kwargs["mass (g)"])
        self.fall = kwargs["fall"]
        self.year = kwargs["year"]
        self.latitude = float(kwargs["reclat"])
        self.longitude = float(kwargs["reclong"])


    def get_year(self):
        return int(self.year[6:10])


    def get_location(self):
        pass


    def __repr__(self):
        return self.name + ", " + str(self.mass) + ", " + str(self.get_year())