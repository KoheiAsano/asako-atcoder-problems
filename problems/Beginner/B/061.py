import sys
N,M = [int(n) for n in input().split()]

a = [0]*M
b = [0]*M
bucket = [0]*N
for i in range(M):
    a[i], b[i] = [int(n)-1 for n in input().split()]
    bucket[a[i]]+=1
    bucket[b[i]]+=1
for i in range(N):
    print(bucket[i])
