from sys import exit
from math import ceil
# A,B,C = [int(n) for n in input().split()]
N = int(input())
ABCDE = [int(input()) for _ in range(5)]
mostn = min(ABCDE)
print(ceil(N/mostn) + 4)
