import sys
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
S = str(input())
# T = str(input())

t = {}
for s in S:
    if not(s in t):
        t[s] = 1
    else:
        t[s]+=1

ans = [n % 2 for n in t.values()]
print("Yes" if 1 not in ans else "No")
