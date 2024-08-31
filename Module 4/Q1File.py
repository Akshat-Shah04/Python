"""
open: Function to open a file and return a file object.
syntax: 
file = open('file_path','mode')

or 

with open('example.txt', 'r') as file:
    for i in file:
        print(i.split())

Modes:
'r' - Read
'w' - Write
'a' - Append
'x' - Create

with: Context manager to handle file operations and ensure files are closed properly.
The open function is versatile and is the primary method used for file I/O operations in Python 3.


"""


