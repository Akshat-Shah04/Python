# Write a Python program to replace last value of tuples in a list.

t = (1, 2, 3, 4, 5, 6, 7)
print("Original Tuple : ", t)
n = int(input("Enter a value : "))
t1 = t[:-1] + (n,)
print("Modified Tuple : ", t1)

"""
Original Tuple :  (1, 2, 3, 4, 5, 6, 7)
Enter a value : 12 
Modified Tuple :  (1, 2, 3, 4, 5, 6, 12)
"""
