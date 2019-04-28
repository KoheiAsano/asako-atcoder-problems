from sys import exit
N,D = [int(n) for n in input().split()]
A = sorted([int(n) for n in input().split()])
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
ans = 0
for i in range(len(A)-D,-1,-D):
    ans+=A[i]
print(ans)
