from sys import exit
import queue
N, M = [int(n) for n in input().split()]

INF = 10**20
map = [[] for _ in range(N)]
dis = [["INF" for _ in range(M)] for __ in range(N)]
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for i in range(N):
    map[i] = list(str(input()))
    for j in range(len(map[i])):
        if(map[i][j] == "S"):
            s = (i, j)
        elif (map[i][j] == "G"):
            g = (i, j)

# print(s, g)


def bfs(s: 'tuple', g: 'tuple') -> 'int':

    Q = queue.Queue()
    Q.put(s)
    dis[s[0]][s[1]] = 0
    # for i in range(len(dis)):
    #     print(dis[i])
    while(not Q.empty()):
        now = Q.get()

        for d in dxy:
            tx, ty = now[0] + d[0], now[1] + d[1]
            if(0 <= tx <= N-1 and 0 <= ty <= M-1
            and (map[tx][ty] == "." or map[tx][ty] == "G")):
                Q.put((tx, ty))
                map[tx][ty] = "#"
                dis[tx][ty] = dis[now[0]][now[1]]+1
    return dis[g[0]][g[1]]


print(bfs(s, g))
