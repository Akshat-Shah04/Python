"""
Write a Python program to read last n lines of a file
"""

filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def read_last_lines(filename, n):
    with open(filename, "r") as file:
        line = file.readlines()
        n_last = line[-n:]
        for i in n_last:
            print(i.strip())


read_last_lines(filename, 3)

"""
I love Python Programming
I am currently solving Module 4.
Hello Akshat Shah!!
"""
