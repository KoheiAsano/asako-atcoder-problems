
N = int(input())
for pt in range((1 << N)):#1 == 線あり 0 == 線なし　とする
    # if "11" in bin(pt): continue
    v = []
    for i in range(N):
        if (1 << i) & pt:
            v.append(i)
    print(v)
