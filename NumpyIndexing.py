# Numpy array Indexing

import numpy as np
arr_1=np.array([[1,2,3,4],[5,6,7,8]])
arr_2=np.array([[[1,2,3,4],[5,6,7,8]],[[2,5,7,8],[9,1,23,4]]])
arr=np.array([1,2,3,4])
print(arr[2])
print(arr[1]+arr[3])
#2-D access(negative idexing)
print(arr_1[1,-2])
#3-D access
print(arr_2[1,1,2])