# from sys import exit
N, M = [int(n) for n in input().split()]
# N = int(input())
a = [(int(n), 1) for n in input().split()]
B = [0 for _ in range(M)]
C = [0 for _ in range(M)]
for i in range(M):
    B[i], C[i] = [int(n) for n in input().split()]
    a.append((C[i], B[i]))

a = sorted(a, key=lambda x: -x[0])
i = 0
ans = 0
# print(a)
while(N != 0):
    num = min(N, a[i][1])
    ans += num*a[i][0]
    # print(num*a[i][0])
    N -= num
    i += 1

print(ans)
