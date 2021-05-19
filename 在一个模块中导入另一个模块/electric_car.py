from car import Car


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
