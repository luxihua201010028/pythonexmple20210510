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


class Battery:
    def __init__(self, battery_size=80):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('my car have a ' + str(self.battery_size) + '  -kwh battery')

    def get_range(self):
        if self.battery_size == 80:
            range_battery = 240
        else:
            range_battery = 270
        message = 'this car can be approximately ' + str(range_battery)
        message += ' miles on a full charge'
        print(message)


class ElectricCar(Car):
    """电动汽车的独到之处"""

    def __init__(self, make, model, year):
        """
        初始化父类属性,在初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
