# Reshape the array from the previous question into a 2x5 matrix. 
import numpy as np
arr = np.arange(1,11)

res = arr.reshape(2,5)
print(res)

'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
'''