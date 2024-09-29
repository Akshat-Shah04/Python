"""
How many except statements can a try-except block have? Name Some built-in exception classes:
When will the else part of try-except-else be executed?
"""

"""
A try-except block in Python can have multiple except statements to handle different types of exceptions. There is no strict limit to the number of except blocks you can include, allowing you to catch and handle various specific exceptions separately.
"""

try:
    a = int(input("Enter a number: "))
    res = 10 / a
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division was successful. The result is:", res)

"""
Enter a number: 2
Division was successful. The result is: 5.0


Enter a number: 0
Error: Cannot divide by zero.


Enter a number: a
Invalid input! Please enter a valid number.

"""

"""
Some Built-in Exception Classes

Exception: The base class for all built-in exceptions. You can use it to catch any exception.

ArithmeticError: Base class for errors that occur for numeric calculations.

ZeroDivisionError: Raised when a division or modulo operation is performed with zero as the divisor.

OverflowError: Raised when the result of an arithmetic operation is too large to be represented.

ValueError: Raised when a function receives an argument of the correct type but with an inappropriate value.

TypeError: Raised when an operation or function is applied to an object of inappropriate type.

IndexError: Raised when trying to access an element from a list, tuple, or string using an index that is out of range.

KeyError: Raised when trying to access a dictionary with a key that does not exist.

FileNotFoundError: Raised when trying to open a file that does not exist.

ImportError: Raised when an import statement fails to find the module definition or when a from import fails to find a name that is being imported.

AttributeError: Raised when an attribute reference or assignment fails.

OSError: Raised for system-related errors, such as file handling, I/O, etc.


When Will the else Part of try-except-else Be Executed?
-> The else part of a try-except-else block will be executed only if no exceptions are raised in the try block. This allows you to specify code that should run if the try block is successful and no errors occur.


"""
