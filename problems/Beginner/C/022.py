import sys

N,M = [int(n) for n in input().split()]
l = [0]*N
r = [0]*N
s = [0]*N
for i in range(N):
    l[i], r[i], s[i] = [int(n) for n in input().split()]
ans = 0
for k in range(1,M+1):
    tmp = 0
    for i in range(N):
        if (l[i] <= k and k<=r[i]):
            continue
        else:
            tmp +=s[i]
    ans = max(ans,tmp)
print(ans)
