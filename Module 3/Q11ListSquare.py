sq = []
for i in range(1,30):
    i = i**2
    sq.append(i)    
res = sq[:5] + sq[-5:]
print(res)

'''
output :
[1, 4, 9, 16, 25, 625, 676, 729, 784, 841]
'''