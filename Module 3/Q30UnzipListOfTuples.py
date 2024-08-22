# Write a Python program to unzip a list of tuples into individual lists.
list_of_tuples = [(1, 'a', 3.2), (2, 'b', 41.5), (3, 'c', 5.9)]
l1, l2, l3 = zip(*list_of_tuples)
l1 = list(l1)
l2 = list(l2)
l3 = list(l3)
print("Unzipped lists:")
print("List 1:", l1)
print("List 2:", l2)
print("List 3:", l3)

'''
Unzipped lists:
List 1: [1, 2, 3]
List 2: ['a', 'b', 'c']
List 3: [3.2, 41.5, 5.9]
'''

