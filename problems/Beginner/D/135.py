from sys import exit, stderr, stdin
input = stdin.readline


def main():
    MOD = 10**9 + 7
    S = input()[:-1]
    L = len(S)
    # 余り
    memo = [0 for _ in range(13)]
    memo[0] = 1

    for i in range(L):
        memo_prev = [x for x in memo]
        memo = [0 for _ in range(13)]
        # 数字なら以前までの余りにたす
        if S[i].isnumeric():
            n = int(S[i])
            for m in range(13):
                cur = (10*m+n)%13
                memo[cur] += memo_prev[m]
        # ?なら1~10の余りのケース全てをためす
        else:
            for n in range(10):
                for m in range(13):
                    cur = (10*m+n)%13
                    memo[cur] += memo_prev[m]
            for m in range(13):
                memo[m] %= MOD
    print(memo[5])


if __name__ == "__main__":
    main()
