# What is tuple? Difference between list and tuple

"""
Tuple is an immutable,indexed and ordered collection of items in python.
Tuples are similar to lists but differ in that tuples cannot be changed (i.e., they are immutable). 
Once a tuple is created, you cannot modify, add, or remove elements from it.

Tuples are defined using parentheses ().
Tuples contain elements of any type (e.g., integers, strings, other tuples, lists, etc.).
"""

t = (1, 2, 3, "apple", [4, 5], (6, 7))
print("Tuple : ", t)

# Tuple :  (1, 2, 3, 'apple', [4, 5], (6, 7))

"""
Difference between Tuple and List:

1. Syntax :
        List : uses square brackets []
        Tuple : uses parantheses ()
2. Mutability :
        List : Mutable
        Tuple : Immutable
3. Methods : 
        List : append(), remove(), sort(), copy(), clear(), count(), extend(), insert(), pop(), min(), max(), reverse(), index()
        Tuple : count(), index()
4. Performance:
        List : Slower
        Tuple : Faster
5. Use Case:
        List : Suitable for collections of data that may change
        Tuple : Suitable for fixed collections of data
6. Memory Usage :
        List : More
        Tuple : Less


"""
