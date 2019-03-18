import sys
N = int(input())
D,X = [int(n) for n in input().split()]
A = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
ans = N
for d in range(2,D+1):
    for a in A:
        if(d % a==1 or a == 1):
            ans+=1
print(ans+X)
