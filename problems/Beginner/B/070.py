import sys
A,B,C,D = [int(n) for n in input().split()]
# N = int(input())
# A = [0]*N
# for i in range(N):
#     A[i] = int(input())
ans = min(B,D) - max(A,C)
print(ans if ans > 0 else 0)
