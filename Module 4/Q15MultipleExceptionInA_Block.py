try:
    a = int(input("Enter a number: "))
    result = 10 / a
except (ValueError, ZeroDivisionError):
    print("An error occurred: Please check your input and try again.")
else:
    print("Division was successful. The result is:", result)


"""
Enter a number: 1.1
An error occurred: Please check your input and try again.


Enter a number: 2
Division was successful. The result is: 5.0


Enter a number: 0
An error occurred: Please check your input and try again.
"""
