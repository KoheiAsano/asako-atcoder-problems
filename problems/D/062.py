import heapq
N = int(input())
A = list(map(int,input().split()))

# 左側
l = A[0:N]
lsum = [sum(l)]
heapq.heapify(l)
# 右側
r = list(map(lambda x: -x, A[-N:]))
rsum = [sum(r)]# (-)
heapq.heapify(r)
for i in range(N,2*N):
    x = heapq.heappushpop(l,A[i])#max when A[i] added
    lsum.append(lsum[-1] + A[i] - x)

    x =  - heapq.heappushpop(r, -A[3*N-1-i])#min when A[i] added
    rsum.append(rsum[-1] - A[3*N-1-i] + x)

ans = -9999999999999999
for i in range(len(rsum)):
    ans = max(ans, lsum[i]+rsum[len(rsum)-1-i])

print(ans)
