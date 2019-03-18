import sys
# A,B,C = [int(n) for n in input().split()]
N = int(input())
a = [0]*N
s = set()

for i in range(N):
    a[i] = int(input())
    if not a[i] in s:
        s.add(a[i])
s = sorted(list(s))
dic = {}
for i,s in enumerate(s):
    dic[s] = i

for i in range(N):
    print(dic[a[i]])
