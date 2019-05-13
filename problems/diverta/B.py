# from sys import exit
R, G, B, N = [int(n) for n in input().split()]
ans = 0
for i in range(3001):
    for j in range(3001):
        le = N - i*R - j*G
        if (le) % B == 0 and le >= 0:
            ans += 1
print(ans)
