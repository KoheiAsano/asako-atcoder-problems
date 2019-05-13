# from sys import exit
# A,B,C = [int(n) for n in input().split()]
N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
ans = 0
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        m = N // i - 1
        if m and N // m == N % m:
            ans += m
print(ans)
