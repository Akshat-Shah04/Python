d = {"a": 1, "b": 2, "c": 3, "d": 4}
n = input("Enter the key : ")
if n in d.keys():
    print(f"{n} key is present in the dictionary")
else:
    print(f"{n} key is not present in the dictionary")


"""

Enter the key : x
x key is not present in the dictionary

Enter the key : a
a key is present in the dictionary

"""
