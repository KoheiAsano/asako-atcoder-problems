from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    # A, B, C = [int(n) for n in input().split()]
    # print(A,B,C)

    L, R = list(map(int,input().split()))

    def count(S):
        LS = len(S)
        # memo[桁][未満==1,ピッタリ==0][4or9がある==1,それ以外==0]
        memo = [[[0 for _ in range(2)] for _ in range(2)] for __ in range(LS+1)]
        memo[0][0][0] = 1
        for i in range(LS):
            D = int(S[i])
            for j in range(2):
                for k in range(2):
                    for d in range(10 if j else D+1):
                            memo[i+1][1 if j or d<D  else 0][1 if k or d == 4 or d == 9 else 0] += memo[i][j][k]
        return memo[LS][0][1] + memo[LS][1][1]

    print(count(str(R)) - count(str(L-1)))


if __name__ == "__main__":
    main()
