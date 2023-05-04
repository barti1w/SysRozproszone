from Point import Point
from Polygon import Polygon

p1 = Point()
print(p1)

p2 = Point(2, 1)
print(p2)

p2 = p2 * 2
print(p2)

p3 = Point(4, 2)
p4 = Point(3, 1)

print(p2 == p3)
print(p2 == p4)

pol1 = Polygon()
pol1.add_point(p1)
pol1.add_point(p2)
pol1.add_point(p3)
pol1.add_point(p4)

print(pol1)
var = pol1[1]
var1 = pol1[1:4:]
var2 = pol1[::-1]
print(var)
print(var1)
print(var2)