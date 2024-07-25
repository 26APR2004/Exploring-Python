import numpy as np
#Dimensions in array
#0-D array
arr_0=np.array(23)
print(arr_0)
print("Dimension:",arr_0.ndim)
# 1-D array
arr_1=np.array([1,2,3,4,5])
print(arr_1)
print(type(arr_1))
print("Dimension:",arr_1.ndim)
# 2-D array
arr_2=np.array([[1,2,3],[4,5,6]])
print(arr_2)
print("Dimension:",arr_2.ndim)
#3-D array
arr_3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr_3)
print("Dimension:",arr_3.ndmin)
