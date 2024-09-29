# Write a Python function that checks whether a passed string is palindrome or not


def palindromeString(str):
    str = str.lower()
    rev = ""
    rev = str[::-1]
    if rev == str:
        return True
    else:
        return False


print(palindromeString("Hello"))
print(palindromeString("Heh"))


"""     
False
True
"""
