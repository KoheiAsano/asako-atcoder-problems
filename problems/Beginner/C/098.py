import sys
# N,M = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())
# a,b,c = [int(n) for n in input().split()]
# ←W, E→
# EEELWWWWにしたい
N = int(input())
S = str(input())
cusum = [0]*N
cusum[0] = 1 if S[0] == 'E' else 0

for i in range(1,N):
    cusum[i] = cusum[i-1]
    if S[i] == 'E':
        cusum[i]+=1
ans = 999999999999
for i in range(N):
    if i == 0:
        tmp = cusum[N-1] - cusum[0]
    elif i == N-1:
        tmp = N-1 - cusum[N-2]
    else:
        tmp = i - cusum[i-1]
        tmp += cusum[N-1] - cusum[i]
    ans = min(tmp, ans)
print(ans)
