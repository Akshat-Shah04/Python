# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1': ['a','b'], '2': ['c','d']}
# Expected Output: ac ad bc bd

d = {"1": ["a", "b"], "2": ["c", "d"]}


def fun1(d):
    keys = list(d.keys())
    str = d[keys[0]]
    for key in keys[1:]:
        new_str = []
        for i in str:
            for letter in d[key]:
                new_str.append(i + letter)
        str = new_str

    for i in str:
        print(i)


print(fun1(d))

"""
ac
ad
bc
bd
"""
