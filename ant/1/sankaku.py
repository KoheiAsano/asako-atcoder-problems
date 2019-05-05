from sys import exit
N = int(input())
a = [int(n) for n in input().split()]
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
def istri(a,b,c):
    l = max([a,b,c])
    if(l > sum([a,b,c]) - l):
        return False
    return True
ans = 0
for i in range(N):
    for k in range(i+1,N):
        for j in range(k+1,N):
            if istri(a[i],a[k],a[j]):
                ans = max(ans, a[i]+a[k]+a[j])
print(ans)
