"""
When Is finally Executed?

No Exception Raised: If the try block completes successfully without raising any exceptions, the finally block will execute after the try block.

Exception Raised and Handled: If an exception is raised in the try block and is caught and handled by an except block, the finally block will still execute after the except block.

Exception Raised and Not Handled: If an exception is raised in the try block and is not caught by any except block, the finally block will execute before the exception is propagated further up the call stack.

"""

try:
    a = int(input("Enter a number: "))
    res = 10 / a
    print("result : ",res)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally : 
    print("Execution Completed..")


'''
Enter a number: 5
result :  2.0
Execution Completed..


Enter a number: 0
Error: Cannot divide by zero.
Execution Completed..

'''