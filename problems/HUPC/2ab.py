# from sys import exit, stderr
# from inspect import currentframe
# def debug(*args):
#     names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
#     print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args), file=stderr)
#     return
INF = 10e10
H, W = [int(n) for n in input().split()]
c = [["" for __ in range(W)] for _ in range(H)]
B = set()
for i in range(H):
    c[i] = list(str(input()))
    for j in range(W):
        if c[i][j] == "B":
            B.add((i,j))


a = 0
b = INF
c = 0
d = INF
for e in B:
    a = max(e[0] + e[1],a)
    b = min(e[0] + e[1],b)
    c = max(e[0] - e[1],c)
    d = min(e[0] - e[1],d)
print(max(a-b, c-d))
