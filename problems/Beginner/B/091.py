import sys
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# S = str(input())
# T = str(input())
total = {}
s = [0]*N
for i in range(N):
    s[i] = str(input())
    if not (s[i] in total):
        total[s[i]] = 1
    else:
        total[s[i]] += 1
M = int(input())
t = [0]*M
for i in range(M):
    t[i] = str(input())
    if not (t[i] in total):
        total[t[i]] = -1
    else:
        total[t[i]] -= 1

ar = total.values()
ans = max(ar)
print(ans if ans>0 else 0)
