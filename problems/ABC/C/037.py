
import sys
N,K = [int(n) for n in input().split()]
a = [int(n) for n in input().split()]

tmp = 0
S = [0]*N
for i in range(N):
    tmp+=a[i]
    S[i]=tmp
ans = S[K-1]
for k in range(K,N):
    ans+=S[k]-S[k-K]

print(ans)
