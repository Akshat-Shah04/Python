# Write a Python program to remove an empty tuple(s) from a list of tuples.
a = [(0,1,2,3),(),(4,5,6,7),(8,9,10),(),(),11,(12,23),(14,14)]
print(f"Length of the list of tuple is : {len(a)}")
b = []
for i in a:
    if i:
        b.append(i)


print(f"Length of the list of tuple (without empty tuple) is : {len(b)}")

'''
Length of the list of tuple is : 9
Length of the list of tuple (without empty tuple) is : 6
'''