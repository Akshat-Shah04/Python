# Write a Python program to map two lists into a dictionary

key = ['name','age','city','university']
val = ['Akshat',20,'Ahmedabad','SOU']

d = dict(zip(key,val))

print(d)

'''
{'name': 'Akshat', 'age': 20, 'city': 'Ahmedabad', 'university': 'SOU'}
'''