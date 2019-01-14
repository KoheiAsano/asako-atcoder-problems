import sys
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
# S = str(input())
# T = str(input())
a,b = [str(n) for n in input().split()]

ab = int(a+b)
table = [n*n for n in range(1,101)]
print("Yes" if ab in table else "No")
