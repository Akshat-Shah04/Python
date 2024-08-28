# Write a Python function to check whether a number is perfect or not.

"""
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is a perfect number because its divisors  are 1, 2, and 3, and 1 + 2 + 3 = 6.
"""


def perfect(n):
    sum = 0
    if n < 1:
        return False

    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum == n:
        return f"{n} is a perfect number"
    else:
        return f"{n} is not a perfect number"


print(perfect(-5))
print(perfect(5))
print(perfect(6))
print(perfect(2))

"""
False
5 is not a perfect number
6 is a perfect number
2 is not a perfect number

"""
