# Write a Python program to check whether an element exists within a tuple.

t = (1, 2, 3, 4, 5, 6, 7, 8)
n = int(input("Enter a number : "))

for i in t:
    if n in t:
        flag = 1
        break
    else:
        flag = 0

if flag == 1:
    print(f"{n} exists in the tuple...")
else:
    print(f"{n} does not exists in the tuple...")

"""
Enter a number : 3
3 exists in the tuple...

Enter a number : 12
12 does not exists in the tuple...
"""
