from sys import exit
N = int(input())
V = [int(n) for n in input().split()]
C = [int(n) for n in input().split()]
VC=[0]*N
for i in range(N):
    VC[i] = (V[i],C[i])
VC = sorted(VC,key=lambda x:-x[0])
ans = 0
for i in range(N):
    if(VC[i][0] > VC[i][1]):
        ans+=VC[i][0] - VC[i][1]
print(ans)
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
