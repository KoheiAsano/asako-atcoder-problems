import sys
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# S = str(input())
# T = str(input())
A = [0]*N
for i in range(N):
    A[i] = int(input())

s = set()
ans = 0
for a in A:
    if a in s:
        ans +=1
    else:
        s.add(a)
print(ans)
