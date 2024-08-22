# Sort the dictionary by value

d = {
        'a':12,
        'b':32,
        'c':1,
        'd':5,
        'e':45
    }

l = list(d.items())
for i in range(len(l)):
    min_index = i
    for j in range(i+1,len(l)):
        if l[j][1] < l[min_index][1]:
            min_index = j
        l[i],l[min_index] = l[min_index],l[i]
s = {}
for k,v in l:
    s[k] = v

s_des = {k:v for k,v in reversed(list(s.items()))}
print("Unsorted : ",d)
print("Sorted(Ascending) : ",s)
print("Sorted(Descending) : ",s_des)
    
    

'''
Here, I have used selection sort.
in which the selected number is swapped with the smallest number in the unsorted array.

'''

'''
Unsorted :  {'a': 12, 'b': 32, 'c': 1, 'd': 5, 'e': 45}
Sorted(Ascending) :  {'c': 1, 'a': 12, 'b': 32, 'd': 5, 'e': 45}
Sorted(Descending) :  {'e': 45, 'd': 5, 'b': 32, 'a': 12, 'c': 1}
'''