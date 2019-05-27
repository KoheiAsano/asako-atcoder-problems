N = int(input())
p = set([int(n) for n in range(2, N+1)])
for i in range(2, int(N**1/2)):
    if i not in p:
        continue

    cnt = 2
    while(N >= i*cnt):
        p.discard(i*cnt)
        cnt += 1

print(p)
