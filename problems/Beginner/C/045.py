S = list(input())
N = len(S)
ans = 0
for pt in range((1 << (N-1))):#1 == 線あり 0 == 線なし　とする
    # if "11" in bin(pt): continue
    tmpS = S.copy()
    # v = []
    inscnt = 1
    for i in range(N-1):
        if (1 << i) & pt:
            tmpS.insert(i+inscnt,'+')
            inscnt+=1
    # print(tmpS)
    tmpsum=eval("".join(tmpS))
    # print(tmpsum)
    ans+=tmpsum
    # print(v)
print(ans)
