class Airline:
    def __init__(self, name):
        self.name = name
        self.fleet = set()

    def getFleet(self):
        return self.fleet

    def setFleet(self, new_plane):
        self.fleet.add(new_plane)

    def __str__(self):
        return "{} has {} in it's fleet".format(self.name, self.fleet)

class Plane():
    def __init__(self, name, capacity, model):
        self.name = name
        self.capacity = capacity
        self.model = model

    def setCapacity(capacity):
        self.capacity = capacity

    def __str__(self):
        return self.name

class Mini_Plane(Plane):
    def __init__(self, name):
        super().__init__(name, 2, "drone")


m747 = Plane("some_name", 75, 747)
airbus = Plane("airbus", 250, "airbus")
drone = Mini_Plane("drone")
print(m747.name)

southwest_airlines = Airline("Southwest Airlines")
american_airlines = Airline("American Airlines")
print(southwest_airlines.name)
print(american_airlines.name)
southwest_airlines.setFleet(m747)southwest_airlines.setFleet(airbus)
print(drone.name)

for plane in southwest_airlines.fleet:
    print(plane)
