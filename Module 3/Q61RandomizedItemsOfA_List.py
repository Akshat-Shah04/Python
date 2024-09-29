# How will you set the starting value in generating random numbers?
import random

a = [1, 2, 3, 4, 5]
for i in range(1, 6):
    random.shuffle(a)
    print(f"Shuffle {i} : {a}")

"""
Shuffle 1 : [5, 1, 4, 3, 2]
Shuffle 2 : [4, 3, 2, 1, 5]
Shuffle 3 : [1, 4, 3, 5, 2]
Shuffle 4 : [5, 1, 3, 2, 4]
Shuffle 5 : [2, 5, 3, 4, 1]
"""
