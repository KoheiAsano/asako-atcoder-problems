import sys
n = int(input())
kind = set(list("abcdefghijklmnopqrstuvwxyz"))
S = str(input())
kind = set(S)
dic = {}
for k in kind:
    dic[k] = S.count(k)

for i in range(n-1):
    S = str(input())
    kind = set(S) & kind
    for k in kind:
        dic[k] = min(S.count(k),dic[k])

kind = sorted(list(kind))
ans = ""
for a in kind:
    ans += a*dic[a]
print(ans)
