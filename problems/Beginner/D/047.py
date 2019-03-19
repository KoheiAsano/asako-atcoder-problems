import sys
N,T = [int(n) for n in input().split()]
# N = int(input())
A = [int(n) for n in input().split()]

minv = 10**10
difmax = 0
ans = 0
for i in range(N):
    minv = min(minv,A[i])
    if(difmax < A[i]-minv):
        difmax = A[i]-minv
        ans = 1
    elif difmax == A[i]-minv:
        ans+=1
print(ans)
