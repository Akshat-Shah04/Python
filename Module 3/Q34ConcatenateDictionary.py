# Write a Python script to concatenate following dictionaries to create a new one.

d1 = {'a':1,'b':2,'c':3}
d2 = {'apple' : 5, 'banana':7}
d3 = {'USA':'Washington D.C.','India':'New Delhi','China':'Beijing'}

l1 = list(d1.items())
l2 = list(d2.items())
l3 = list(d3.items())
l4 = l1
l4.extend(l2)
l4.extend(l3)

d = {k:v for k,v in l4}
print("Dictionary 1 : ",d1)
print("Dictionary 2 : ",d2)
print("Dictionary 3 : ",d3)
print("Concatenated Dictionary is : ",d)


'''
Dictionary 1 :  {'a': 1, 'b': 2, 'c': 3}
Dictionary 2 :  {'apple': 5, 'banana': 7}
Dictionary 3 :  {'USA': 'Washington D.C.', 'India': 'New Delhi', 'China': 'Beijing'}
Concatenated Dictionary is :  {'a': 1, 'b': 2, 'c': 3, 'apple': 5, 'banana': 7, 'USA': 'Washington D.C.', 'India': 'New Delhi', 'China': 'Beijing'}
'''