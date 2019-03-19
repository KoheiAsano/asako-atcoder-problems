import sys
N = int(input())

a = [int(n) for n in input().split()]

dic = {}
for ak in a:
    if not(ak in dic):
        dic[ak] = 1
    else:
        dic[ak] += 1
ans = 0
for k in dic.keys():
    if(dic[k] - k > 0):
        ans+=dic[k] - k
    elif(dic[k] - k < 0):
        ans+=dic[k]
print(ans)
