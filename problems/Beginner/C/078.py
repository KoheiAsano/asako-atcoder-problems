from sys import exit
N,M = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# L = len(S)
# T = str(input())

constant = (N-M)*100

print((2**M)*(1900*M + constant))
exit()
