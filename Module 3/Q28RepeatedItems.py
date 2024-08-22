# Write a Python program to find the repeated items of a tuple.
t = (1,1,2,3,4,5,6,2,5,2)
k = {}
for i in t:
    if i in k:
        k[i] += 1
    else :
        k[i] = 1

l = []
for item,count in k.items():
    if count > 1:
        l.append(item)
    else:
        pass
print("Original Tuple : ",t)    
print("List of Repeated Items of Tuples is : ",l)


'''
Original Tuple :  (1, 1, 2, 3, 4, 5, 6, 2, 5, 2)
List of Repeated Items of Tuples is :  [1, 2, 5]
'''    