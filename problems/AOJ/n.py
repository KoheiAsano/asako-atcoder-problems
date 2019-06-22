# A, B, C = [int(n) for n in input().split()]
while(True):
    N = int(input())
    if N == 0:
        break
    k = [int(n) for n in input().split()]
    dic = dict(zip([ i for i in range(len(k))], k))
    ans = 0
    for i in range(len(k)):
        if k[i] > 0:
            k[i] -= 1
            ans += 1
    print(ans + 1 if max(k) > 0 else "NA")
