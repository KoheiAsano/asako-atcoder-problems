def num(n):
    return n*(n+1)//2

from sys import exit
N, K = [int(n) for n in input().split()]
if num(N-2) < K:
    print(-1)
    exit()
# 1をハブにしてつぶす
cnt = num(N-2) - K
print(N-1 + cnt)
for i in range(2, N+1):
    print(1, i)



while(cnt != 0):
    for i in range(2, N+1):
        for j in range(i+1, N+1):
            print(i, j)
            cnt -= 1
            if cnt == 0:
                exit()
