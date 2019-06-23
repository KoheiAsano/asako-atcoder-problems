from sys import exit
INF = 10**21
N = int(input())
AB = [0 for i in range(N)]

for i in range(N):
    AB[i] = [int(n) for n in input().split()]
AB = sorted(AB, key=lambda x: x[0])
AB = sorted(AB, key=lambda x: -x[1])

now = AB[0][1]
for i in range(len(AB)):
    now = min(AB[i][1], now)
    now -= AB[i][0]
if now < 0:
    print("No")
    exit()
else:
    print("Yes")
