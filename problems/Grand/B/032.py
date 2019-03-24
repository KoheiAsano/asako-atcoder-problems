from sys import exit
from numpy.random import rand
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
N = int(input())
# dic = {}
# for i in range(1,N+1):
#     dic[i] = 0
#偶数ならN+1をつくる
ansgroup = []
if N%2 == 0:
    for i in range(1,N//2+1):
        ansgroup.append([i, N-i+1])
else:
    for i in range(1,N//2+1):
        ansgroup.append([i, N-i])
    ansgroup.append([N])
nodesum = 0
ans = []
for i in range(len(ansgroup)):
    for j in range(i+1,len(ansgroup)):
        for e1 in ansgroup[i]:
            for e2 in ansgroup[j]:
                nodesum+=1
                ans.append([e1,e2])
print(nodesum)
for a in ans:
    print(a[0],a[1])
# ansset = set([ i for i in range(1,N+1)])
# tmpset = set()
# for i in range(1,len(ans)):
#     if ans[i-1][0] == ans[i][0]:
#         tmpset = ans[i][1] | ans[i-1][1]
#     else:
#         print(ans[i-1][0],ansset)
#         ansset = set([ i for i in range(1,N+1)])
# exit()
#奇数ならNをつくる組みあわせがペアそれ以外とぜんぶつながる
