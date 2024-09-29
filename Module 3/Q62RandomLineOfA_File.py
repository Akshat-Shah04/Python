# How will you randomizes the items of a list in place?

import random


def random_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        r = random.choice(lines)
        return r.strip()


filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 3\\Demo.txt"
)
for i in range(1, 4):
    line = random_line(filename)
    print(f"Shuffle {i} : {line}")


"""
Shuffle 1 : I am currently 20 years old.
Shuffle 2 : I am studying in Silver Oak University
Shuffle 3 : I am studying in Silver Oak University

"""

"""
Demo.txt

My name is Akshat Shah
I am currently 20 years old.
I reside in Ahmedabad
I am studying in Silver Oak University
My dream is to travel to various countries in the world.

"""
