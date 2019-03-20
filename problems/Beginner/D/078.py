from sys import exit
N,Z,W = [int(n) for n in input().split()]
a = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# L = len(S)
# T = str(input())
if N == 1:
    print(abs(W-a[N-1]))
else:
    print(max(abs(a[N-1]-a[N-2]), abs(W-a[N-1])))
