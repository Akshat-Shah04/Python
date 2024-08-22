# Write a Python function to reverses a string if its length is a multiple of 4.
str = input("Enter a string : ")
length = len(str)
if length % 4 == 0:
    rev_str = str[::-1]
    print(f"Reversed String is : {rev_str}")
else:
    print("Not a Multiple of 4!!!")
    print(str)

"""
Output :

Enter a string : AkshatSh  
Reversed String is : hStahskA

Enter a string : Akshat
Not a Multiple of 4!!!
Akshat




"""