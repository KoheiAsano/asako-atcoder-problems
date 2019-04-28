from collections import defaultdict
H,W,N = [int(n) for n in input().split()]
# N = int(input())
dxy = [[0,0],[1,0],[0,1],
[-1,0],[0,-1],[1,1],
[-1,-1], [1,-1], [-1,1]]

effdic = defaultdict(int)
for i in range(N):
    a,b = [int(n)-1 for n in input().split()]
    for d in dxy:
        ta, tb = a+d[0], b+d[1]
        if(1 <= ta < H-1 and 1 <= tb < W-1):
            effdic[(ta,tb)] += 1
print((H-2)*(W-2) - len(effdic))
for i in range(1,10):
    tmp=0
    for v in effdic.values():
        if(v == i):
            tmp+=1
    print(tmp)
