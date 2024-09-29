"""
Explain Exception handling? What is an Error in Python?
"""

"""
Exception handling is a mechanism in Python that allows a programmer to manage errors or exceptional conditions that occur during the execution of a program. Instead of the program terminating unexpectedly, exception handling provides a way to catch and handle errors gracefully, allowing the program to continue running or exit cleanly.

Key Concepts in Exception Handling:

Exception:
An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

Try Block:
The try block contains the code that might raise an exception. If an exception occurs within this block, the execution is transferred to the corresponding except block.

Except Block:
The except block catches and handles the exception that occurred in the try block. You can specify the type of exception to catch, or you can catch all exceptions using a general except block.

Finally Block:
The finally block is optional and contains code that should run no matter what—whether an exception was raised or not. It is often used for cleanup tasks, such as closing files or releasing resources.
"""

"""
An error in programming refers to a problem or issue in the code that prevents the program from running correctly. Errors can occur for various reasons, such as incorrect syntax, logic mistakes, or unexpected conditions during execution. In Python, errors are generally categorized into two main types: syntax errors and runtime errors.


Syntax Errors: Syntax errors occur when the code is written incorrectly according to the rules of the programming language. These errors are detected by the Python interpreter before the program runs.

Runtime Errors: Runtime errors occur while the program is running. These errors happen due to invalid operations or conditions that arise during the execution of the program. Unlike syntax errors, runtime errors are not detected until the code is actually executed.



Types of Common Errors in Python:
SyntaxError, ZeroDivisionError, TypeError, ValueError, NameError, IndexError, KeyError, AttributeError, ImportError
"""


def divide(a, b):
    try:
        res = a / b
        print("Result : ", res)
    except ZeroDivisionError:
        print("Denominator cannot be 0.")

    except TypeError:
        print("Input must be in numbers only..")


print("-----------------------")
divide(12, 0)
print("-----------------------")
divide(12, 3)
print("-----------------------")
divide(10, "a")
print("-----------------------")

"""

-----------------------
Denominator cannot be 0.       
-----------------------        
Result :  4.0
-----------------------        
Input must be in numbers only..
-----------------------        

"""
