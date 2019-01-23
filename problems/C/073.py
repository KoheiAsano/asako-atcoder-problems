import sys
N = int(input())
A = [0]*N
s = set()
for i in range(N):
    A[i] = int(input())
    if(A[i] in s):
        s.remove(A[i])
    else:
        s.add(A[i])
print(len(s))
