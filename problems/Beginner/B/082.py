from sys import exit
import math
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = list(input())
T = list(input())
S = "".join(sorted(S))
T = "".join(sorted(T)[::-1])
print("Yes" if S<T else "No")
# L = len(S)
# T = str(input())
