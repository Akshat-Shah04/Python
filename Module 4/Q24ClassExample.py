"""
Write a Python class named Circle constructed by a radius and two methods which will compute 
the area and the perimeter of a circle
"""


class Circle:
    global PI
    PI = 3.14

    def __init__(self, r):
        self.r = r

    def area(self):
        return PI * self.r * self.r

    def perimeter(self):
        return 2 * PI * self.r


res = Circle(12)
print(f"Area of Circle is : {res.area()}")
print(f"Perimeter of Circle is : {res.perimeter()}")

"""
Area of Circle is : 452.15999999999997
Perimeter of Circle is : 75.36
"""
