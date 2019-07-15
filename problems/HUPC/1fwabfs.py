from collections import deque
N, W = [int(n) for n in input().split()]
P = [int(n) for n in input().split()]
adjl = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, c = [int(n) for n in input().split()]
    adjl[u-1].append((v-1, c))
    adjl[v-1].append((u-1, c))
templatevisited = [False for _ in range(N)]
templatedist = [0 for _ in range(N)]
Q = deque()
ans = 0

for s in range(N):
    visited = templatevisited.copy()
    dist = templatedist.copy()
    val = templatedist.copy()
    val[s] = P[s]
    visited[s] = True
    Q.appendleft((s, 0))
    while(len(Q) != 0):
        now = Q.pop()
        for n in adjl[now[0]]:
            if visited[n[0]]:
                continue
            dist[n[0]] += dist[now[0]] + n[1]
            visited[n[0]] = True
            if dist[n[0]] > W:
                continue
            val[n[0]] = val[now[0]] + P[n[0]]
            Q.appendleft(n)
    ans = max(max(val), ans)
print(ans)
