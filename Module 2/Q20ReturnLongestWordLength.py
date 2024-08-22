# Write a Python function that takes a list of words and returns the length of the longest one.

words = []
str = input("Enter a string : ")
for i in str.split(' '):
    words.append(i)
print("List of the words entered :", words)

def longest_word(l):
    max_length = max(len(word) for word in words)
    return max_length

print("Length of longest word is : ",longest_word(words))


"""

output : 

Enter a string : Akshat Shah AkshatShah Hello World HelloWorld!
List of the words entered : ['Akshat', 'Shah', 'AkshatShah', 'Hello', 'World', 'HelloWorld!']
Length of longest word is :  11

"""