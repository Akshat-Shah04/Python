# How will you create a dictionary using tuples in python?

# Method 1 : using dict()
t = [(1, "Akshat"), (2, "Raj"), (3, "Arya"), (4, "Suraj")]
m1 = dict(t)
print("Tuple to dictionary...")
print("Method 1 : ", m1)

# Method 2 : using tuple as an argument
t2 = ((1, "Akshat"), (2, "Raj"), (3, "Arya"), (4, "Suraj"))
m2 = dict(t2)
print("Method 2 : ", m2)

# Using dictionary comprehension

m3 = {key: value for key, value in t2}
print("Method 3 : ", m3)

"""
Tuple to dictionary...
Method 1 :  {1: 'Akshat', 2: 'Raj', 3: 'Arya', 4: 'Suraj'} 
Method 2 :  {1: 'Akshat', 2: 'Raj', 3: 'Arya', 4: 'Suraj'} 
Method 3 :  {1: 'Akshat', 2: 'Raj', 3: 'Arya', 4: 'Suraj'} 
"""
