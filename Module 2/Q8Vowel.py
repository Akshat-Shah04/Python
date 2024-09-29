# Write a Python program to test whether a passed letter is a vowel or not
c = input("Enter a character : ").lower()
char = c.lower
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(f"{c} is a vowel.")
else:
    print(f"{c} is a consonant.")

"""

O/P:
Enter a character : a
a is a vowel.

Enter a character : C
C is a consonant.

"""
