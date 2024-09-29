"""
Write a Python program to generate and print a list of first and last 5 elements where 
the values are square of numbers between 1 and 30.
"""

sq = []
for i in range(1, 30):
    i = i**2
    sq.append(i)
res = sq[:5] + sq[-5:]
print(res)

"""
output :
[1, 4, 9, 16, 25, 625, 676, 729, 784, 841]
"""
