n = int(input())
w = [0 for _ in range(n)]
v = [0 for _ in range(n)]
for i in range(n):
    w[i], v[i] = list(map(int, input().split()))
W = int(input())

memo = [[0 for _ in range(8)] for __ in range(5)]
for cur in range(n):
    for cap in range(W+1):
        if w[cur] > cap:
            memo[cur+1][cap] = memo[cur][cap]
        else:
            memo[cur+1][cap] = max(memo[cur+1][cap-w[cur]] + v[cur], memo[cur][cap])
print(memo[n][W])
