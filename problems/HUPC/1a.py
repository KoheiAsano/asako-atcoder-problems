# from sys import exit

N = int(input())
P = [int(n) for n in input().split()]
t = [int(n) for n in input().split()]
Pt = sorted([(p, t) for p, t in zip(P,t)])

memo = [0 for _ in range(N)]
def rec(n):
    if n >= N:
        return 0
    elif memo[n] != 0:
        return memo[n]
    else:
        memo[n] = min([rec(n+t[i]) + P[i] for i in range(4)])
        return memo[n]
print(rec(0))
