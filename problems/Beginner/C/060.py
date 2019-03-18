import sys
N,T = [int(n) for n in input().split()]
t = [int(n) for n in input().split()]
ans = 0
for i in range(N-1):
    if(t[i+1]-t[i] < T):
        ans+=t[i+1]-t[i]
    else:
        ans+=T

ans+=T
print(ans)
