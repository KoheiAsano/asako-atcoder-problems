from sys import exit
N,K = [int(n) for n in input().split()]
K-=1
h = [int(input()) for _ in range(N)]
h = sorted(h)
minm = 10**9
# print(h)

for i in range(0,N-K):
    # print(h[i],h[i+K])
    if h[i+K]-h[i] < minm:
        minm = h[i+K]-h[i]
print(minm)
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
