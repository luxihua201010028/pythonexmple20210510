class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odo = 20

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
    def increment_odo(self,miles):
        self.odo+=miles

# my_new_car = Car('audi', 'a4', 2016)
# my_new_car.year=1000
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odo(200)
# my_new_car.read_odo()
my_used_car = Car('subaru', 'a4', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odo(23500)
my_used_car.read_odo()
my_used_car.increment_odo(500)
my_used_car.read_odo()