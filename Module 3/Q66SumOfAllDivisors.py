# Write a Python program to returns sum of all divisors of a number


def sum_divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum


n = int(input("Enter a number : "))
print("Sum : ", sum_divisors(n))

# Enter a number : 6
# Sum :  12
