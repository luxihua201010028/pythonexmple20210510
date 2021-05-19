from car import Car
from electric_car import ElectricCar #优化导入之后的结果

my_beetle = Car('volkswagen', 'beetle', 2000)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
