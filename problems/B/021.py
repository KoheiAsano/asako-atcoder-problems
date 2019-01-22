import sys
N = int(input())
ab = [int(n) for n in input().split()]
K = int(input())
P = [int(n) for n in input().split()]
s = set(ab)
for p in P:
    if p in s:
        print("NO")
        sys.exit()
    else:
        s.add(p)
print("YES")
