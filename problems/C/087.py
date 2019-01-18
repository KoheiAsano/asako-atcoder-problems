import sys
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# S = str(input())
# T = str(input())
A0 = [int(n) for n in input().split()]
A1 = [int(n) for n in input().split()]

ans = 0
for c in range(N):
    tmp=0
    for n in range(N):
        if(c>n):
            tmp+=A0[n]
        elif(c==n):
            tmp+=A0[n]
            tmp+=A1[n]
        else:
            tmp+=A1[n]
    ans = max(ans,tmp)
print(ans)
