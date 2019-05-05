from sys import exit
N,M = [int(n) for n in input().split()]
map = [[] for __ in range(N)]
v = [[ False for i in range(M)] for __ in range(N)]

for i in range(N):
    map[i] = list(str(input().split()))
dxy = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
def dfs(x,y):
    if(v[y][x]):return False
    else: v[y][x] = True
    if(map[y][x] == "W"):
        map[y][x] = "."
        for d in dxy:
            if(0 <= x+d[0] <=M-1 and 0 <= y+d[1] <=N-1):
                dfs(x+d[0],y+d[1])
        return True
    else: return False
ans = 0
for i in range(N):
    for j in range(M):
        if dfs(j,i):
            ans+=1
print(ans)
