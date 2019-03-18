import sys
A,B,K = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())

i = 1
cnt = 1
factor = [0]*100
for i in range(1,101):
    if(A%i == 0 and B%i == 0):
        factor.append(i)
factor = sorted(factor)
print(factor[-K])
