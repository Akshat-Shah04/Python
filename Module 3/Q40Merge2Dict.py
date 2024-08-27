# Write a Python script to merge two Python dictionaries

def merge(d1,d2):
    d1.update(d2)
    return d1

d1 = {'name': 'Akshat', 'age': 20}
d2 = {'city': 'AMD', 'country': 'INDIA'}

print(merge(d1,d2))

# {'name': 'Akshat', 'age': 20, 'city': 'AMD', 'country': 'INDIA'}