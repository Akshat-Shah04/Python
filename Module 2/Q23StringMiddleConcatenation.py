"""
Write a Python function to insert a string in the middle of a string.
"""

str = input("Enter a String : ")
word = input(f"Enter the word you want to enter in the string '{str}': ")
length = len(str) // 2
new_str = str[:length] + word + str[length:]
print(f"New String is : {new_str}")

"""
Output :

Enter a String : hello world
Enter the word you want to enter in the string 'hello world': hurrah
New String is : hellohurrah world


"""
