# How can you pick a random item from a list or tuple?
import random

fruits = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Strawberry",
    "Grapes",
    "Pineapple",
    "Blueberry",
    "Watermelon",
    "Kiwi",
]
r = random.choices(fruits)
print(r)


"""
['Strawberry']
['Apple']
['Watermelon']
['Strawberry']
"""
