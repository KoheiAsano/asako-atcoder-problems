import numpy as np
N = int(input())
a = []
b = []

for n in range(N):  # input
    a.append([float(n) for n in input().split()])

for n in range(N):
    b.append(float(input()))
a = np.array(a)
b = np.array(b)

print(np.linalg.solve(a,b))

def printmat():
    for i in range(N):
        print(a[i], b[i])
    print()


# print(a)
# print(a[1:])
# # 前進
for k in range(N):
    for i in range(k+1, N):
        m = a[i][k]/a[k][k]
        a[i][k+1:] = a[i][k+1:] - m*a[k][k+1:]
        b[i] = b[i]- m*b[k]

print(a)
res = []
for k in range(N-1, -1, -1):
    sum = 0
    for i in range(N-1, k, -1):
        sum += a[k][i]*res[-1]
    res.append((b[k]-sum)/a[k][k])
print(a)
print(res[::-1])
