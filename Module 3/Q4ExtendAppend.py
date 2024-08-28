"""
Difference between append() and extend()
"""

# Using append method
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)

# Output: [1, 2, 3, [4, 5]]

# Using extend method
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

# Output: [1, 2, 3, 4, 5]

"""
append method adds a single element to the end of the list.
append() takes one argument (the element to add), which can be any type (another list, a number, a string, etc.).


extend method adds each element of an iterable (like a list or tuple) to the end of the list.
extend() takes an iterable (like a list, string, tuple, etc.).



Use append() when you want to add a single element to a list.
Use extend() when you want to add multiple elements from an iterable to a list individually.
"""
