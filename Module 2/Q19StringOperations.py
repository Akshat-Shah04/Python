"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.
"""

str = input("Enter a string: ")

f_not = str.find("not")
f_poor = str.find("poor")

if f_not > f_poor:
    result = str[:f_poor] + "good" + str[f_not + 3 :]
else:
    result = str

print("Modified string:", result)


"""
output :

Enter a string: poor man is not in right way
Modified string: good in right way

"""
