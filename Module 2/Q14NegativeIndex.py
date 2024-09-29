"""
Q14) What are negative indexes and why are they used?
Ans. Negative indexes in Python provide a way to access elements from the end of a sequence, such as a list, tuple, or string. They offer a convenient and intuitive way to reference elements relative to the end of the sequence without needing to calculate the exact positive index.

=> Negative indexes count from the end of the sequence. An index of -1 refers to the last element, -2 refers to the second-to-last element, and so on.

=>  Uses of Negative Indexes : 

    -> Convenience: They provide a simple way to access elements relative to the end of the sequence without having to compute the length of the sequence.

    -> Readability: When working with sequences where you need to access the last few elements frequently, negative indexes can make the code more readable and straightforward.
    -> Reverse :  We can use negative index to print a list or tuple in reverse order too.



"""

fruits = ["apple", "banana", "cherry", "kiwi"]
print(fruits)
print(fruits[-1])
print(fruits[-2])
# reverse order
print(fruits[::-1])


"""
Output:

['apple', 'banana', 'cherry', 'kiwi']
kiwi
cherry
['kiwi', 'cherry', 'banana', 'apple']


"""
