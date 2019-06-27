from sys import exit
INF = 10**21
N, L= [int(n) for n in input().split()]
apples = [L +i - 1 for i in range(1,N+1)]
ans = INF
val = INF
# print(apples)
for i in range(N):
    eat = apples[i]
    tmp = abs(eat)
    if tmp < val:
        ans = sum(apples) - eat
        val = tmp
print(ans)
