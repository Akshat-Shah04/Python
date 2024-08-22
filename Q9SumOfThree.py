# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))

if(n1 == n2 or n2 == n3 or n1 == n3):
    sum = 0
    print("Due to condition mentioned in the question when two of the three numbers are equal, Sum must be 0.")
else:
    sum = n1 + n2 + n3
print(f"Sum of 3 numbers is {sum}.")

'''

O/P:

Enter number 1 : 12
Enter number 2 : 12
Enter number 3 : 5
Due to condition mentioned in the question when two of the three numbers are equal, Sum must be 0.
Sum of 3 numbers is 0.



Enter number 1 : 1
Enter number 2 : 4
Enter number 3 : 50
Sum of 3 numbers is 55.

'''