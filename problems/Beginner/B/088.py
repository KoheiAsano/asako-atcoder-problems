from sys import exit
# A,B,C = [int(n) for n in input().split()]
N = int(input())
a = sorted([int(n) for n in input().split()], key=lambda x:-x)
ali = 0
bob = 0
for i in range(N):
    if i % 2 == 0:
        ali +=a[i]
    else:
        bob +=a[i]
print(ali-bob)
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
exit()
