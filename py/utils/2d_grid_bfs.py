from collections import deque
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
INF = (1 << 21)
H, W = [int(n) for n in input().split()]
ans = 0
# Map
Map = [[0 for _ in range(W)] for __ in range(H)]
# 歩数
D = [[INF for _ in range(W)] for __ in range(H)]
for h in range(H):
    Map[h] = list(input())
# print(Map)
# print(ans)

def bfs(s):
    q = deque()
    q.append(s)
    D[s[0]][s[1]] = 1
    while(not q.empty()):
        u = q.pop()
        for d in dxy:
            v = [u[0] + d[0], u[1] + d[1]]
            if (v[0] < 0 or v[1] < 0 or v[0] >= H or v[1] >= W
            or Map[v[0]][v[1]] == "#"):
                continue
            if (D[v[0]][v[1]] != INF):
                continue
            D[v[0]][v[1]] = D[u[0]][u[1]] + 1
            q.append(v)
bfs([0, 0])
# for th in ran
