N = int(input())
C = [int(input()) for _ in range(N-1)]

asum = [0]*(N)
asum[0] = 0
for i in range(1,N):
    if(C[i-1]>0):
        asum[i]=asum[i-1] + C[i-1]
    else:
        asum[i]=max(0,asum[i-1] + C[i-1])

C = C[::-1]
rasum = [0]*(N)
rasum[0] = 0
for i in range(1,N):
    if(C[i-1]>0):
        rasum[i]=rasum[i-1] + C[i-1]
    else:
        rasum[i] = max(0,rasum[i-1] + C[i-1])

rasum = rasum[::-1]
for i in range(N):
    print(max(asum[i],rasum[i]))
