from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    # A, B, C = [int(n) for n in input().split()]
    # print(A,B,C)
    S = str(input()).rstrip()
    LS = len(S)
    cand = set()
    cur = 0
    memo = [[0 for _ in range(2)] for __ in range(LS)]
    memo[0][0] = 1
    memo[0][1] = int(S[0])
    for i in range(LS-1):
        D = int(S[i+1])
        for j in range(2):
            for d in range(10 if j else D+1):
                memo[i+1][1 if j or d<D  else 0] += memo[i][j]
    print(memo)


if __name__ == "__main__":
    main()
