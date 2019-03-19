import sys
W,H,N = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
field = [[1 for _ in range(H)] for _ in range(W)]
x = [0]*N
y = [0]*N
a = [0]*N# 1 == 左の面、2 == 右, 3 == 下 4 == 下
for i in range(N):
    x[i], y[i], a[i] = [int(n) for n in input().split()]
    if(a[i] == 1):
        for k in range(x[i]):
            field[k] = [0 for _ in range(H)]
    elif(a[i] == 2):
        for k in range(x[i],W):
            field[k] = [0 for _ in range(H)]
    elif(a[i] == 3):
        for k in range(W):
            for j in range(y[i]):
                field[k][j] = 0
    elif(a[i] == 4):
        for k in range(W):
            for j in range(y[i],H):
                field[k][j] = 0
    # for k in range(W):
        # print(field[k])
ans = 0
for i in range(W):
    ans+=sum(field[i])
    # print(field[i])
print(ans)
