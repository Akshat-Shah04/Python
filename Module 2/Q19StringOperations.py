"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.
"""

str = input("Enter a string: ")

first_not = str.find('not')
first_poor = str.find('poor')

if first_not > first_poor:
    result = str[:first_poor] + 'good' + str[first_not + 3:]
else:
    result = str

print("Modified string:", result)


"""
output :

Enter a string: poor man is not in right way
Modified string: good in right way

"""