"""
In Python, functions can be categorized in two main types:

1. Built-in Functions: These are pre-defined functions that are part of the Python language. You can use them directly without any additional setup. Examples include print(), len(), range(), type(), and many more.

2. User-defined Functions: These are functions that you create yourself to perform a specific task. You define them using the def keyword

3. Lambda Functions (Anonymous Functions): These are small, one-line functions created using the lambda keyword. They are often used for simple operations and can be passed as arguments to other functions
"""

# Built-In

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Lenght of list : ", len(l))
print("Type : ", type(l))

# User-defined


# With parameters and with return type
def sum1(a, b):
    return a + b


# Without parameters and without return type
def sum2():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print("Sum : ", a + b)


# Without parameters and with return type
def sum3():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    return a + b


# With parameters and without return type
def sum4(a, b):
    print("Sum : ", a + b)


print("Sum : ", sum1(100, 150))
sum2()
print("Sum : ", sum3())
sum4(10, 20)

# Lambda Function:

max_number = lambda a, b: a if a > b else b
result1 = max_number(5, 3)
result2 = max_number(25, 30)
print(f"The maximum number is: {result1}")
print(f"The maximum number is: {result2}")


"""
Lenght of list :  10
Type :  <class 'list'>

Sum :  250

Enter a:10
Enter b:50
Sum :  60

Enter a:12
Enter b:5
Sum :  17

Sum :  30

The maximum number is: 5
The maximum number is: 30

"""
