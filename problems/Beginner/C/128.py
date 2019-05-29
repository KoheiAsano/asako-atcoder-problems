# from sys import exit
N, M = [int(n) for n in input().split()]
ss = [0 for i in range(M)]
for i in range(M):
    ss[i] = set([int(n)-1 for n in input().split()][1:])
p = [int(n) for n in input().split()]
ans = 0
for pt in range((1 << N)):# 1 == 線あり 0 == 線なし　とする
    each = [0]*M
    for i in range(N):
        if (1 << i) & pt:
            for iss in range(len(ss)):
                if i in ss[iss]:
                    each[iss] +=1
    OK = True

    for i in range(len(each)):
        if each[i]%2 != p[i]:
            OK = False
    if OK:
        ans += 1
print(ans)
