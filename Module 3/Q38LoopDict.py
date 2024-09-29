# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
d = {}
j = 1001
for i in range(1, 16):
    d[i] = j
    j += 1

for k, v in d.items():
    print(f"{k} : {v}")

"""
1 : 1001
2 : 1002 
3 : 1003 
4 : 1004 
5 : 1005 
6 : 1006 
7 : 1007 
8 : 1008 
9 : 1009 
10 : 1010
11 : 1011
12 : 1012
13 : 1013
14 : 1014
15 : 1015

"""
