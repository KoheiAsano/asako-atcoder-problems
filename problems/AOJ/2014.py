from collections import deque
dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def which(x, y, map):
    if(map[x][y] != "."):
        return (True, 0)
    else:
        Q = deque()
        W, H = len(map[0]), len(map)
        map[x][y] = "#"
        Q.append((x, y))
        Black, White = False, False
        res = 1
        while(len(Q) != 0):
            now = Q.popleft()
            for d in dxy:
                tx, ty = now[0]+d[0], now[1]+d[1]
                # 色判定もする
                if 0 <= tx <= H-1 and 0 <= ty <= W-1:
                    if map[tx][ty] == ".":
                        map[tx][ty] = "#"
                        res += 1
                        Q.append((tx, ty))
                    elif map[tx][ty] == "B":
                        Black = True
                    elif map[tx][ty] == "W":
                        White = True
    # 黒かどうかと、レス、無効ならTrue 0
    return (Black, res) if Black ^ White else (True, 0)


while(True):
    # .だけBFSする、Wにしかぶつからないで全部いけたらW
    W, H = [int(n) for n in input().split()]
    V = [[False for _ in range(W)]for __ in range(H)]
    if W+H == 0:
        break
    map = ["" for _ in range(H)]
    for i in range(H):
        map[i] = list(str(input()))
    b = 0
    w = 0
    for i in range(H):
        for j in range(W):
            Black, cnt = which(i, j, map)
            if Black:
                b += cnt
            else:
                w += cnt
    # for i in range(H):
    #     print(map[i])
    print(b, w)
