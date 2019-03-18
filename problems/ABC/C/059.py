import sys
N = int(input())
a = [int(_) for _ in input().split()]

#+,-,+,-
asum = [0]*(N)
ansp = 0
if(a[0] <= 0):
    ansp+=1-a[0]
    asum[0]=1
else:
    asum[0] = a[0]
for i in range(1,N):
    asum[i] = asum[i-1] + a[i]
    if(asum[i-1]*asum[i] >= 0):
        if(asum[i-1]>0):
            ansp+=1+asum[i]
            asum[i]=-1
        else:
            ansp+=1-asum[i]
            asum[i]=1
# print(asum)
# print(ansp)
#-,+,-,+,,,
ansn = 0
if(a[0] >= 0 ):
    ansn+=1+a[0]
    asum[0]=-1
else:
    asum[0] = a[0]
for i in range(1,N):
    asum[i] = asum[i-1] + a[i]
    if(asum[i-1]*asum[i] >= 0):
        if(asum[i-1]>0):
            ansn+=1+asum[i]
            asum[i]=-1
        else:
            ansn+=1-asum[i]
            asum[i]=1
# print(asum)
# print(ansn)
print(min(ansp,ansn))
