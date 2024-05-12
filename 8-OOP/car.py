class Car:

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " has stopped")


# from car import Car

# car_1 = Car("Chevy", "Corvette", "2021", "blue")
# car_2 = Car("Ford", "Mustang", "2022", "Red")

# print("Make: " + car_2.make)
# print("Model: " + car_2.model)
# print("Year: " + car_2.year)
# print("Colour: " + car_2.colour)

# car_2.drive()
# car_2.stop()
