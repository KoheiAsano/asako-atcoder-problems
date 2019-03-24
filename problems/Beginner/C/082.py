from sys import exit
import math
N = int(input())
dic = {}
a = [int(n) for n in input().split()]
for e in a:
    if e in dic:
        dic[e]+=1
    else:
        dic[e] = 1
ans = 0
for k in dic.keys():
    if k < dic[k]:
        ans+=dic[k]-k
    elif k > dic[k]:
        ans+=dic[k]
    else:
        continue
print(ans)
