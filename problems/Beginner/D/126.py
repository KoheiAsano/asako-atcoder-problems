from collections import deque
N = int(input())
INF = 10**12
# tree = [[INF for _ in range(N)]for __ in range(N)]
tree = [[]for __ in range(N)]

for i in range(N-1):
    u, v, w = [int(n) for n in input().split()]
    u -= 1
    v -= 1
    tree[u].append((v, w))
    tree[v].append((u, w))

color = [INF for __ in range(N)]
treedist = [INF for __ in range(N)]


def bfs(s):
    q = deque()
    q.append(s)
    color[s[0]] = 0
    treedist[s[0]] = 0
    while(len(q) != 0):
        u = q.pop()
        for near in tree[u[0]]:
            if treedist[near[0]] != INF:
                continue
            treedist[near[0]] = treedist[u[0]] + near[1]
            if treedist[near[0]] % 2 == 0:
                color[near[0]] = 0
            else:
                color[near[0]] = 1
            q.append(near)

# print(tree)

bfs((u, v))
# print(u, v)
# print(treedist)
for i in range(len(color)):
    print(color[i])
