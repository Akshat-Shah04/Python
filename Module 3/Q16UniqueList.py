def noDuplicates(li):
    s = set(li)
    return list(s)

li = [1,1,1,1,3,4,0,0,2,3,4,100,99]
print("Modified List : ",noDuplicates(li))
'''
o/p:

Modified List :  [0, 1, 2, 3, 4, 100, 99]
'''