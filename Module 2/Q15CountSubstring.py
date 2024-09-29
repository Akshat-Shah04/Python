# Write a Python program to count occurrences of a substring in a string.

str = input("Enter a string : ")
substring = input(f"Enter the substring of String '{str}' :")
count = str.count(substring)
print(f"Count of {substring} in String '{str}' is {count}")


"""
O/P :

Enter a string : hello world hello hello world
Enter the substring of String 'hello world hello hello world' :hello
Count of hello in String 'hello world hello hello world' is 3       

"""
