import sys
# A,B,C = [int(n) for n in input().split()]
# n,X = [int(n) for n in input().split()]
N = int(input())
# S = str(input())
# T = str(input())
h = (int(N / 3600))
N %= 3600
m = (int(N / 60))
N %= 60
s = (int(N))
print("{:0=2}:{:0=2}:{:0=2}".format(h,m,s))
