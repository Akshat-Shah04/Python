"""
Write a Python program to create a dictionary from a string.
o Note: Track the count of the letters from the string. Sample string: 'w3resource'
Expected output: {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""

str1 = "w3resource"
str2 = "AkshatShah"
def countStr(str):
    l = []
    for i in str:
        l.append(i)

    count = 0
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(countStr(str1))
print(countStr(str2))


'''
{'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
{'A': 1, 'k': 1, 's': 1, 'h': 3, 'a': 2, 't': 1, 'S': 1}

'''