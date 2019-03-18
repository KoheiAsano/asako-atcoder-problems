import sys
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
S = str(input())
# T = str(input())
ans = ""
for s in S:
    if s == "B":
        ans = ans[:-1]
    else:
        ans += s

print(ans)
