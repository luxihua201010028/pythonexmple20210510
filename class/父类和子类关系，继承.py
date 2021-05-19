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
    def increment_odo(self,miles):
        self.odo+=miles
class Eletricar(Car):
    '''电动汽车的独到之处'''
    def __init__(self,make,model,year):
        '''初始化父类属性'''
        super().__init__(make,model,year)
        self.batrery=70
    def describle_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print('my car have a '+str(self.batrery)+'  -kwh battery')
    def fill_gas_tank(self):
        print('this car does not need  GAS TANK')
    
my_tesla=Eletricar('tesla','model s',2018)
print(my_tesla.get_descriptive_name())

my_tesla.describle_battery()