n = int(input())
w = [0 for _ in range(n)]
v = [0 for _ in range(n)]
for i in range(n):
    w[i], v[i] = list(map(int, input().split()))
W = int(input())

# memo = [[-1 for _ in range(10002)] for __ in range(102)]
memo = [[0 for _ in range(6)] for __ in range(6)]

for cur in range(n-1, -1, -1):
    for cap in range(W+1):
        if cap < w[cur]:
            memo[cur][cap] = memo[cur+1][cap]
        else:
            memo[cur][cap] = max(memo[cur+1][cap-w[cur]]+v[cur], memo[cur+1][cap])
print(memo[0][W])

# for i in range(n):
#     print(w[i], v[i])
# for i in range(n+1):
#     print(i, memo[i])
