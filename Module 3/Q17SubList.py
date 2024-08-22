l1 = [1,2,3,4,5,6,7]
l2 = [3,4,7,6]

for i in l2:
    if i in l1:
        flag = True
    else:
        flag = False
        break

if flag == True:
    print("List",l2," present in",l1)
else:
    print("List",l2,"not present in",l1)
    

"""
List [3, 4, 7, 6]  present in [1, 2, 3, 4, 5, 6, 7]
"""
    
    
    