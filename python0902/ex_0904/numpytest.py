import numpy as np

# arr = np.array([1, 2, 3])
# print(arr)
# print(type(arr))

# #0차원
# arr0 = np.array(100)
# #1차원
# arr1 = np.array([1, 2, 3])
# #2차원[행, 열]
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# #3차원[면, 행, 열]
# arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

# print(arr0.ndim)
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0, 1])
print(arr[1, 4])
print(arr[1, -1])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[0, 1, 2])
