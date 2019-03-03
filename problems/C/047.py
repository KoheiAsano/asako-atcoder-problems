import sys
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
# L = len(S)
# T = str(input())
ans = 0
prev = S[0]
for s in S:
    if(s != prev):
        ans+=1
    prev = s
print(ans)
