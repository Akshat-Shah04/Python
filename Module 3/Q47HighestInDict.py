# Write a Python program to find the highest 3 values in a dictionary
d = {"a": 81, "b": 20, "c": 31}
k = []
for i in d.values():
    k.append(i)

k = sorted(k)
print("Maximum Value is :", k[-1])

'''
Maximum Value is : 81

'''