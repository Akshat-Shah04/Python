# Write a Python program to count the occurrences of each word in a given sentence
str = input("Enter a string : ").lower()
found_list = []
words = []
words = str.split(" ")
for i in words:
    count = words.count(i)
    if i not in found_list:
        found_list.append(i)
        print(f"{i} is repeated {count} times.")
    else:
        pass

"""
output :
Enter a string : hello hello world
hello is repeated 2 times.
world is repeated 1 times.

"""
