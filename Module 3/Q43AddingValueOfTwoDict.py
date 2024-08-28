"""
Write a Python program to combine two dictionary adding values for common keys.
o d1 = {'a': 100, 'b': 200, 'c':300} 
o d2 = {'a': 300, 'b': 200,'d':400}
• Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}).
"""

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 100, "b": 200, "d": 400}
for i, j in d1.items():
    if i in d2.items():
        print(i)

for x, y in d2.items():
    if x not in d1.items():
        d1[x] = y
print(d1)
