from sys import exit
import bisect

N = int(input())
A = sorted([int(n) for n in input().split()])
B = sorted([int(n) for n in input().split()])
C = sorted([int(n) for n in input().split()])
Cl = len(C)
# print(A)
# print(B)
# print(C)
ans=0
for b in B:
    a = bisect.bisect_left(A,b)#未満を探す
    c = Cl - bisect.bisect_right(C,b)#以下を探して全体から引く
    # print(b,a,c)
    ans+=a*c
print(ans)
