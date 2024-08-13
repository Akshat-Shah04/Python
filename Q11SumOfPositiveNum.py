# Write a python program to sum of the first n positive integers.
n = int(input("Enter the n positive numbers : "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(f"Sum is {sum}")

'''
O/P:
Enter the n positive numbers : 5
Sum is 15

'''
