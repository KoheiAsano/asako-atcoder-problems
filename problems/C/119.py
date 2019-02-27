import sys
N,A,B,C = [int(n) for n in input().split()]
# N = int(input())
l = [int(input()) for _ in range(N)]
# S = str(input())
# T = str(input())
INF = 10 **18
def dfs(p,a,b,c):
    if p == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a,b,c) > 0  else INF
    ans0 = dfs(p+1,a,b,c)
    ans1 = dfs(p+1,a+l[p],b,c) + 10
    ans2 = dfs(p+1,a,b+l[p],c) + 10
    ans3 = dfs(p+1,a,b,c+l[p]) + 10
    return min(ans0,ans1,ans2,ans3)

print(dfs(0,0,0,0))
