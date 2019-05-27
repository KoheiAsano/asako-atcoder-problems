# from sys import exit
N, M = [int(n) for n in input().split()]
L = [0]*M
R = [0]*M
imos = [0 for _ in range(N+1)]
for i in range(M):
    L[i], R[i] = [int(n) for n in input().split()]
    imos[L[i]-1] += 1
    imos[min(R[i], N)] -= 1

for i in range(1,N+1):
    imos[i] = imos[i-1] + imos[i]

ans = 0
for i in range(len(imos)):
    if imos[i] == M:
        ans += 1

print(ans)
