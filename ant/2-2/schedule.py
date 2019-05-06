N = int(input())
S = [int(n) for n in input().split()]
T = [int(n) for n in input().split()]
ST = sorted(list(zip(S, T)), key=lambda x: x[1])

# print(ST)

tmpt = 0
ans = 0
for st in ST:
    if tmpt < st[0]:
        ans += 1
        tmpt = st[1]
print(ans)
