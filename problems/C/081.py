import sys
# A,B,C = [int(n) for n in input().split()]
N,K = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())
A = [int(n) for n in input().split()]
dic = {}
for a in A:
    if not(a in dic):
        dic[a]=1
    else:
        dic[a]+=1
val = sorted(dic.values())
rc = len(val) - K
ans = 0
for r in range(rc):
    ans += val[r]
print(ans if ans >=0 else 0)
