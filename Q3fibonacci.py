# Write a Python program to get the Fibonacci series of given range
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        nT = fib[-1] + fib[-2]
        fib.append(nT)
    return fib[:n]

n = int(input("Enter the range : ")) 
print(fibonacci(n))

'''

O/P:
Enter the range : 5
[0, 1, 1, 2, 3]

'''