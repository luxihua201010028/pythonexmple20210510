class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odo = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odo(self):
        print('this car is ' + str(self.odo) + ' miles on it')

    def update_odo(self, mileage):
        if mileage >= self.odo:
            self.odo = mileage
        else:
            print("you can't roll back an odo")

    def increment_odo(self, miles):
        self.odo += miles