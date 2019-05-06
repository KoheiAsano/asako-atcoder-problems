# from sys import exit
C1, C5, C10, C50, C100, C500, A = [int(n) for n in input().split()]
V = [500, 100, 50, 10, 5, 1]
Cs = [C500, C100, C50, C10, C5, C1]
ans = 0
for i in range(len(V)):
    t = min(A//V[i], Cs[i])
    A -= t*V[i]
    ans += t

print(ans)
