try:
    a = int(input("Enter a number: "))
    result = 10 / a
except (ValueError, ZeroDivisionError):
    print("An error occurred: Please check your input and try again.")
else:
    print("Division was successful. The result is:", result)


"""

"""
