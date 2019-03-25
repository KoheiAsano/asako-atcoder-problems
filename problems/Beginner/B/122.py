from sys import exit
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
# L = len(S)
cnt = 0
maxs = 0
for s in S:
    if s in ["A","G","C","T"]:
        cnt+=1
    else:
        cnt = 0
    if cnt > maxs:
        maxs = cnt
print(maxs)
