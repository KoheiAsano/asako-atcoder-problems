import sys
A,B,C = [int(n) for n in input().split()]
K = int(input())
ans = A+B+C + max(A,B,C)*(2**K-1)

print(ans)
