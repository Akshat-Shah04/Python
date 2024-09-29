"""
Write a Python program to read a file line by line store it into a variable
"""

filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def file_var(filename):
    with open(filename, "r") as file:
        line = file.readlines()
        return line


a = file_var(filename)
print(a)

"""
['My name is Akshat Shah\n', 'I am currently 20 years old.\n', 'I reside in Ahmedabad\n', 'I am studying in Silver Oak University\n', 'My dream is to travel to various countries in the world.\n', 'I love Python Programming\n', 'I am currently solving Module 4.\n', 'Hello Akshat Shah!!\n']

"""
