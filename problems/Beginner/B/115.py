from sys import exit
# A,B,C = [int(n) for n in input().split()]
N = int(input())
P = [int(input()) for _ in range(N)]
P = sorted(P)
P[-1] = P[-1]//2
print(sum(P))
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
