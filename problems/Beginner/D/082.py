from sys import exit
from collections import defaultdict
import itertools
S = str(input())
x,y = [int(n) for n in input().split()]

dx = []
dy = []
X = True
tmp = 0


S = [len(s) for s in S.split("T")]
dx = S[0::2]
dy = S[1::2]
x -= dx[0]
del dx[0]

def check(d, p):
    memo = set([0])
    for t in d:
        memo = {a+b for a,b in itertools.product(memo, [-t, t])}
    return (p in memo)


print("Yes" if check(dx,x) and check(dy,y) else "No")
