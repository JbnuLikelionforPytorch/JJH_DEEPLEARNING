import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape)
# 일차원은 행으로 바로 들어간다
B = np.array([7,8])
print(B.shape)

pd = np.dot(A, B)
print(pd)
