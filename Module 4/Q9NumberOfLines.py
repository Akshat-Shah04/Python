"""
Write a Python program to count the number of lines in a text file.

"""

filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def count_lines(filename):
    with open(filename, "r") as file:
        line = file.readlines()
        return len(line)


print("Number of Lines in the file is : ", count_lines(filename))

"""
Number of Lines in the file is :  8
"""
