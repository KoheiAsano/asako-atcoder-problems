from sys import exit
# A, B, C = [int(n) for n in input().split()]
N = int(input())
a = [int(n) for n in input().split()]
ans_a = sorted(a)
Q = int(input())
ans = -1

missed = 0
for i in range(N):
    if a[i] != ans_a[i]:
        missed += 1
if missed == 0:
    print(0)
    exit()

for _ in range(Q):
    x, y = [int(n) for n in input().split()]
    if a[x-1] == ans_a[x-1]:
        missed += 1
    if a[y-1] == ans_a[y-1]:
        missed += 1
    if a[x-1] == ans_a[y-1]:
        missed -= 1
    if a[y-1] == ans_a[x-1]:
        missed -= 1
    if missed == 0:
        ans = _ + 1
        break
print(ans)
