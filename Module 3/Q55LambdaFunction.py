# A lambda function in Python is a small anonymous function defined with the lambda keyword. It can take any number of arguments but has only one expression
max_number = lambda a, b: a if a > b else b
result = max_number(5, 3)
print(f"The maximum number is: {result}")


"""
An incomplete version of a function is often referred to as a "stub". A stub is a placeholder function that is not fully implemented but allows the rest of the program to be tested or run without errors.

Stubs usually contain just enough code to allow the program to compile and run, often returning default values or simple messages like "Not implemented yet". Stubs are typically used during development and are later replaced with fully implemented functions.
"""


def calculate_area_of_circle(radius):
    # This is just a placeholder for now
    print("calculate_area_of_circle function is not implemented yet.")
    return None


radius = 5
area = calculate_area_of_circle(radius)

if area is None:
    print("The area could not be calculated because the function is not yet implemented.")
else:
    print(f"The area of the circle with radius {radius} is: {area}")
