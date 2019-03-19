
H,W,K = [int(n) for n in input().split()]
memo = [[0 for _ in range(W)] for __ in range(H+1)]
memo[0][0] = 1
MOD = 10**9 + 7
for h in range(1,H+1):
    for pt in range((1 << W-1)):#1 == 線あり 0 == 線なし　とする
        # pts = bin(pt)[2:]
        # pts = pts[::-1]#反転
        if "11" in bin(pt): continue
        #各パターンの時の各線の計算
        goto = [i for i in range(W)]
        for i in range(W):
            if (1 << i) & pt:
                goto[i], goto[i + 1] = goto[i + 1], goto[i]
        for i in range(W):
            memo[h][goto[i]] += memo[h-1][i]
            memo[h][goto[i]] %= MOD


print(memo[H][K-1])
