import sys
from scipy.sparse.csgraph import floyd_warshall
# import time
#
# start = time.time()

N,M = [int(n) for n in input().split()]
INF = 10**9
ex1graph = [[INF if _ != __ else 0 for _ in range(N-1)] for __ in range(N-1)]
u = [0]*M
v = [0]*M
l = [0]*M
one2i = [INF]*(N-1)
#1から各点のみ別で保存

for i in range(M):
    u[i], v[i], l[i] = [int(n) for n in input().split()]
    if(u[i] != 1):
        ex1graph[u[i]-2][v[i]-2] = l[i]
        ex1graph[v[i]-2][u[i]-2] = l[i]
    else:
        one2i[v[i]-2]=l[i]

# 1以外でわしゃふろ
# def apsp():
#     for k in range(N-1):
#         for i in range(N-1):
#             if ex1graph[i][k] == INF: continue
#             for j in range(N-1):
#                 if ex1graph[k][j] == INF: continue
#                 ex1graph[i][j] = min(ex1graph[i][j], ex1graph[i][k] + ex1graph[k][j])
# apsp()
ex1graph = floyd_warshall(ex1graph)

# for i in range(len(ex1graph)):
#     print(ex1graph[i])
ans = INF
for i in range(N-1):
    for j in range(i+1,N-1):
        if(one2i[i] != INF):
            ans = min(ans,one2i[i] + ex1graph[i][j] + one2i[j])
print(int(ans) if ans != INF else -1)

# end = time.time()
# print(end - start)
