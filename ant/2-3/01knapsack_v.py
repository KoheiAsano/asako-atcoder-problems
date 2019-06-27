n = int(input())
w = [0 for _ in range(n)]
v = [0 for _ in range(n)]
for i in range(n):
    w[i], v[i] = list(map(int, input().split()))
W = int(input())
INF = 10000000002
memo = [[INF for _ in range(10002)] for __ in range(6)]
memo[0][0] = 0

for cur in range(n):
    for val in range(10002):
        if val < v[i]:
            memo[cur+1][val] = memo[cur][val]
        else:
            memo[cur+1][val] = min(memo[cur][val-v[cur]] + w[cur], memo[cur][val])
ans = 0
for val in range(10002):
    ans = val if memo[n][val] <= W else ans
print(ans)
# for cur in range(6):
#     print(cur, memo[cur][:12])
