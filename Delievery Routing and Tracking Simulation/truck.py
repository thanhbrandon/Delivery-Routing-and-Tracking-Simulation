class Truck:

    def __init__(self, id, packages , departTime):
        self.id = id
        self.packages = packages
        self.departTime = departTime

        self.location = "4001 South 700 East",
        self.mileage = 0.0
        self.speed = 18

    def __str__(self):
        return (f"Truck ID: {self.id}, Truck Speed: {self.speed}, Mileage: {self.mileage}, "
                f"Current Location: {self.location}, Packages: {self.packages} , "
                f"Time of Departure: {self.departTime}")   
