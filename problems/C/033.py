import sys
# A,B,C = [int(n) for n in input().split()]
S = str(input())
S.split("+")
# print(S.split("+"))
ans = 0
for s in S.split("+"):
    if("0" in s):
        continue
    else:
        ans+=1
print(ans)
