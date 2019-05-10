N = int(input())
R = int(input())
X = [int(n) for n in input().split()]

ans = 0
i = 0
while(i < N):
    tmp = X[i]
    i += 1
    while(i+1 < N and X[i] <= tmp + R):
        i += 1
    p = X[i-1]
    while(i < N and X[i] < p + R):
        i += 1
    ans += 1

print(ans)
