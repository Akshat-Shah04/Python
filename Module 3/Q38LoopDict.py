d = {}
j = 1001
for i in range(1,16):
    d[i] = j
    j+=1
    
for k,v in d.items():
    print(f"{k} : {v}")
