n = int(input())
m = int(input())
s, t = str(input()), str(input())

memo = [[0 for _ in range(m+1)] for __ in range(n+1)]


for s_cur in range(n):
    for t_cur in range(m):
        c = 1 if s[s_cur] == t[t_cur] else 0
        memo[s_cur+1][t_cur+1] = max(memo[s_cur][t_cur+1], memo[s_cur+1][t_cur], memo[s_cur+1][t_cur] + c)
# for i in range(n+1):
#     print(memo[i])
memo[n][m]
