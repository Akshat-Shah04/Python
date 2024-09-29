# Write a Python program to find the second smallest number in a list.
def second_min(li):
    return sorted(li)


li = [1, 2, 10, 99, 44, 0, -8, -100]
n = second_min(li)
print("Second Smallest Number of list is : ", n[1])
"""
output : Second Smallest Number of list is :  -8

"""
