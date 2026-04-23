import numpy as np

A = np.array([
    [1, 3, 2, 3],
    [6, 2, 5, 4],
    [7, 1, 8, 9],
], dtype=np.int32)

print(A)

B = np.array([
    [4,3,2,1],
    [5,6,7,8]
],
)

print(F"B.T=\n{B.T}")
print(F"B.T.shape={B.T.shape}")

result = A @ B.T
print(F"result=\n{result}")

