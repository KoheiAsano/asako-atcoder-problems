import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
N = int(input())
a = []
b = []

for n in range(N):  # input
    a.append([float(n) for n in input().split()])

for n in range(N):
    b.append(float(input()))
a = np.array(a)
b = np.array(b)
LU = lu(a)[1:]


# Ly = b
y = []
for k in range(N):
    sum = 0
    for i in range(0, k):
        sum += LU[0][k][i]*y[-1]
    y.append((b[k]-sum)/LU[0][k][k])

# Ux = y
res = []
for k in range(N-1, -1, -1):
    sum = 0
    for i in range(N-1, k, -1):
        sum += LU[1][k][i]*res[-1]
    res.append((y[k]-sum)/LU[1][k][k])
print(res[::-1])
print(lu_solve(lu_factor(a), b))
