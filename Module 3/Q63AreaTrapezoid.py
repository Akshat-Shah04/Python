# W.A.P to calculate the area of trapezoid
b1 = int(input("Enter the length of Base 1 : "))
b2 = int(input("Enter the length of Base 2 : "))
h = int(input("Enter the height : "))

def area_trapezoid(b1,b2,h):
    return (b1+b2)*(0.5)*(h)

print("Area of Trapezoid is : ",area_trapezoid(b1,b2,h))

'''
Enter the length of Base 1 : 45
Enter the length of Base 2 : 12
Enter the height : 8  
Area of Trapezoid is :  228.0

'''