import heapq
N, W = [int(n) for n in input().split()]
tmpw = 0
tmpv = 0
minheap = []
for i in range(N):
    w, v = [int(n) for n in input().split()]
    if(w < 0):
        tmpw += w
        tmpv += v
        w *= -1
        v *= -1
    if(v > 0):
        if w == 0:
            tmpv += v
        else:
            heapq.heappush(minheap, (-(v/w), w, v))
while(W-tmpw > 1e-9 and not minheap == []):
    p = heapq.heappop(minheap)
    w = p[1]
    v = p[2]
    x = min(1, (W-tmpw)/w)
    tmpw += x*w
    tmpv += x*v
print(tmpv)
