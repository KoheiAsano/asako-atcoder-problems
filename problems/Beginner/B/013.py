import sys
# A,B,C = [int(n) for n in input().split()]
# n,X = [int(n) for n in input().split()]
a = int(input())
b = int(input())
# S = str(input())
# T = str(input())
ans = abs(a-b)
print(ans if ans < 5 else 10 - ans)
