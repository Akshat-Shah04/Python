# Write a Python program to calculate surface volume and area of a cylinder.
PI = 3.14


def volume(r, h):
    return PI * r * r * h


def area(r, h):
    return (2 * PI * r * h) + (2 * PI * r * r)


r = float(input("Enter radius of the cylinder : "))
h = float(input("Enter height of the cylinder : "))

print(f"Surface Area of Cylinder is : {area(r,h)}")
print(f"Volume of the Cylinder is : {volume(r,h)}")

"""
Enter radius of the cylinder : 5.5
Enter height of the cylinder : 12  
Surface Area of Cylinder is : 604.45
Volume of the Cylinder is : 1139.82

"""
