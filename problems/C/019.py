import sys
# A,B,C =
N = int(input())
a = [int(n) for n in input().split()]
# S = str(input())
# L = len(S)
# T = str(input())

s = set()
ans = 0
for e in a:
    while(e%2 ==0):
        e =int(e/2)
    if not e in s:
        s.add(e)

print(len(s))
