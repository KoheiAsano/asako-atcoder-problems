import sys
# A,B,C = [int(n) for n in input().split()]
N = 4
a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
print(min(a[0],a[1]) + min(a[2],a[3]))
