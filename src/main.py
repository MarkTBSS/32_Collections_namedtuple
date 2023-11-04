""" from collections import namedtuple

Point = namedtuple('Point','x,y')
print(Point)
print("========================")
point12 = Point(1,2)
print(point12)
print(point12.x)
print(point12.y)
print("========================")
point34 = Point(3,4)
print(point34)
print(point34.x)
print(point34.y)
print("========================")
dotProduct = (point12.x * point34.x) + (point12.y * point34.y)
print(dotProduct) """

from collections import namedtuple

Car = namedtuple('Car','Price Mileage Colour Class')
print(Car)
print("========================")
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print(xyz)
print("========================")
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz.Class)
print("========================")