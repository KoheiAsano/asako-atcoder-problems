n = int(input())
w = [0 for _ in range(n)]
v = [0 for _ in range(n)]
for i in range(n):
    w[i], v[i] = list(map(int, input().split()))
W = int(input())

# memo = [[-1 for _ in range(10002)] for __ in range(102)]
memo = [[-1 for _ in range(6)] for __ in range(5)]


def rec(cur, cap):
    if cur >= n:
        return 0
    elif memo[cur][cap] >= 0:
        pass
    elif v[cur] > cap:
        memo[cur][cap] = rec(cur+1, cap)
    else:
        memo[cur][cap] = max(rec(cur+1, cap-w[cur]) + v[cur], rec(cur+1, cap))
    return memo[cur][cap]


print(rec(0, W))
# for i in range(n):
#     print(w[i], v[i])
# for i in range(n):
#     print(i, memo[i])
