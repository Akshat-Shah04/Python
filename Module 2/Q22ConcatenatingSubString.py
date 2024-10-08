"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
- Sample String: w3resource' 
- Expected Result: 'w3ce' 
- Sample String: 'w3' 
- Expected Result: 'w3w3' 
- Sample String: ' w' 
- Expected Result: Empty String

"""

str = input("Enter a String : ")

if len(str) == 2:
    result = str * 2
elif len(str) < 2:
    result = ""
else:
    result = str[:2] + str[-2:]

print(f"Original String is : {str}")
print(f"Expected String is : {result}")


"""
Output: 

Enter a String : Akshat 
Original String is : Akshat
Expected String is : Akat


"""
