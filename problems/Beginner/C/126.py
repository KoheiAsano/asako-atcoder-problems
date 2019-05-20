from math import log, ceil
N, K = [int(n) for n in input().split()]
ans = 0
for i in range(1, N+1):
    tmpans = ceil(log(K/i, 2))
    if tmpans < 0:
        ans += 1/N
    else:
        ans += 1/N * (1/2)**tmpans
print(ans)
