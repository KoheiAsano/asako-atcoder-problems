N, W, H = [int(n) for n in input().split()]


xmap = [0 for _ in range(W+1)]
ymap = [0 for _ in range(H+1)]
for i in range(N):
    x, y, w = [int(n) for n in input().split()]
    l = max(x-w, 0)
    r = min(x+w, W)
    a = max(y-w, 0)
    b = min(y+w, H)
    xmap[l] += 1
    xmap[r] -= 1
    ymap[a] += 1
    ymap[b] -= 1
# print(xmap, ymap)
covered = 0
xcovered = True
for i in range(W):
    covered += xmap[i]
    if covered <= 0:
        xcovered = False
covered = 0
for i in range(H):
    covered += ymap[i]
    if covered <= 0 and not xcovered:
        print("No")
        exit()
print("Yes")
