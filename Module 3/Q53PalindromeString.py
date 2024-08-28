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
