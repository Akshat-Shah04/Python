"""
Write a Python function that takes a list and returns a new list 
with unique elements of the first list.
"""


def unique_ele(li):
    uniq = []
    for element in li:
        if element not in uniq:
            uniq.append(element)
    return uniq


a = [1, 2, 2, 3, 4, 4, 5]
unique = unique_ele(a)
print("Unique elements:", unique)


"""
output :
Unique elements: [1, 2, 3, 4, 5]
"""
