# What is List? How will you reverse a list?

"""
Answer : 
List is an ordered, mutable and indexed data type in python that allows us to store multiple values in it.
List allows duplicate value
We can store different types of data in a single list
 Example : a = [1,2,3,4.54,"Akshat Shah",False,"Hell@o"]
If we know index of a value in a list we can modify its value.
List allows us to append, pop, remove, reverse, index, count, copy, clear, insert, extend, sort methods
"""

a = [1, 2, 3, 4, 5]
print(f"Original list : {a}")


def reverseList(a):
    return a[::-1]


rev = reverseList(a)
print("Reversed List : ", rev)

"""
O/P:

Original list : [1, 2, 3, 4, 5]
Reversed List :  [5, 4, 3, 2, 1]

"""
