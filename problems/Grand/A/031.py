from sys import exit
L = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
dic = {}
for s in S:
    if not s in dic:
        dic[s] = 1
    else:
        dic[s]+=1
ans =1
for d in dic.keys():
    ans*=dic[d]+1
print(ans-1)
