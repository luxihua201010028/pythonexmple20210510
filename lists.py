# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# for item in range(0, len(bicycles)):
#     bicycles[item] = bicycles[item].title()
# print(bicycles)
# bicycles.append('peter')
# print(bicycles)
# bicycles.insert(1, 'mali')
# print(bicycles)
# del bicycles[1]
# print(bicycles)
# bicycles.pop()
# print(bicycles)
# bicycles.pop(2)
# print(bicycles)
# bicycles.remove('Cannondale')
# print(bicycles)
cars = ['bow', 'audi', 'toyota', 'subaru']
print(cars)
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars,reverse=True))
# print(cars)

cars.reverse()
print(cars)
print(len(cars))
listA = list(range(1, 20, 2))
print(listA)
print(min(listA), max(listA), sum(listA))
square = [value**2 for value in range(1, 11)]
print(square)
print(square[-3:])
players = ['charles', 'martins', 'michael', 'eli']
for play in players[:3]:
    print(play.title())
    print(type(play))
