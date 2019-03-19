import sys
# A,B,C = [int(n) for n in input().split()]
N,M = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())
N %= 12
N *= 30
N += M/2
M *= 6
tmp = abs(M-N)
print(180 - tmp%180 if tmp > 180 else tmp)
