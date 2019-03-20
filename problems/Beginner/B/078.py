from sys import exit
X,Y,Z = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# L = len(S)
# T = str(input())
ans = 0
b = max(Y,Z)
while(X>b):
    ans+=1
    X-=Z
    X-=Y
print(ans-1 if X<Z else ans)
exit()
