n, k = map(int,input().split())
s = [int(input()) for _ in range(n)]
if 0 in s:
    ans = n
else:
    ans = 0
    acc = 1 # procuct of s_i in [l,r]
    l = 0
    for r in range(n): # [l,r]
        acc *= s[r]
        if k < acc:
            acc /= s[l]
            l += 1
        ans = max(ans, r - l + 1)
print(ans)
