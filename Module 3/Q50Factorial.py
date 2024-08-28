def fact(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return "None"
    else:
        return n * fact(n - 1)


num = int(input("Enter a number : "))
print(f"Factorial of {num} is {fact(num)}")

"""
Enter a number : 5
Factorial of 5 is 120
"""
