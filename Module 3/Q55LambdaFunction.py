# What is lambda function in python? What we call a function which is incomplete version of a function?

"""
A lambda function in Python is a small anonymous function defined with the lambda keyword. It can take any number of arguments but has only one expression
"""
max_number = lambda a, b: a if a > b else b
res = max_number(5, 3)
print(f"The maximum number is: {res}")


"""
An incomplete version of a function is often referred to as a "stub". A stub is a placeholder function that is not fully implemented but allows the rest of the program to be tested or run without errors.

Stubs usually contain just enough code to allow the program to compile and run, often returning default values or simple messages like "Not implemented yet". Stubs are typically used during development and are later replaced with fully implemented functions.
"""


def calc_ar_circle(radius):
    # This is just a placeholder for now
    print("function is not implemented yet.")
    return None


radius = 5
area = calc_ar_circle(radius)

if area is None:
    print("The area could not be calculated because the function is not implemented.")
else:
    print(f"The area of the circle with radius {radius} is: {area}")
