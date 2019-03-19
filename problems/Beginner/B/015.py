import sys
import math
N = int(input())
A = [int(n) for n in input().split() if n != "0"]
print(math.ceil(sum(A)/len(A)))
# A = [0]*N
# for i in range(N):
#     A[i] = int(input())
