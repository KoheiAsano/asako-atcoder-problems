from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(str(type(var)) + name +":" + " = " + repr(var), file=stderr)
    return


def main():
    N, K = list(map(int,input().split()))
    K = bin(K)[2:].zfill(51)
    a = list(map(int,input().split()))
    for i in range(len(a)):
        a[i] = bin(a[i])[2:].zfill(51)
    # memo[決めた桁目(上位から)][K未満 == 1 not == 0] = そのときの最大値
    memo = [0 for __ in range(51)]
    LT = False
    for i in range(51):
        val = 0
        br = 0
        # 1と0の場合,ただしKのi桁目と超えたかにもよって0だけ
        for b in range(2 if LT or K[i] == '1' else 1):
            valtmp = 0
            for n in a:
                valtmp += b ^ int(n[i])
            if val < valtmp :
                br = b
                val = valtmp
        memo[i] = val
        LT = br < int(K[i]) or LT


    p = 1
    ans = 0
    for i in range(50,-1,-1):
        ans += p*memo[i]
        p *= 2
    print(ans)


if __name__ == "__main__":
    main()
