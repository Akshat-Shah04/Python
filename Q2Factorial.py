# Write a Python program to get the Factorial number of given number.

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
       return n * factorial(n-1)

n = int(input("Enter a number : "))
fact = factorial(n)
print(f"Facorial of {n} is : {fact}")

'''

O/P:
Enter a number : 5
Facorial of 5 is : 120

'''