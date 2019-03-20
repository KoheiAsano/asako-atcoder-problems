from sys import exit
# A,B,C =
G = [[int(n) for n in input().split()]for _ in range(3)]#H,W
ptr = [ [0,1],[1,2], [0,2]]
e1 = G[0][0] - G[1][0]#a1 - a2
for p in ptr:
    e = G[0][p[0]] - G[0][p[1]]
    for h in range(1,3):
        if(e !=G[h][p[0]] - G[h][p[1]]):
            print("No")
            exit()
for p in ptr:
    e = G[p[0]][0] - G[p[1]][0]
    for w in range(1,3):
        if(e !=G[p[0]][w] - G[p[1]][w]):
            print("No")
            exit()
print("Yes")
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
exit()
