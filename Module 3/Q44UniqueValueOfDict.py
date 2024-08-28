# Write a Python program to print all unique values in a dictionary.
d = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 1,
    "f": 10,
    "g": 5,
    "h": 3,
    "i": 6,
}
count = set()
for val in d.values():
    count.add(val)

print(count)

"""
{1, 2, 3, 5, 6, 10}
"""
