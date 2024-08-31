class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


res = Rectangle(12, 15)
print("Area of Rectangle is : ", res.area())

"""
Area of Rectangle is :  180
"""


