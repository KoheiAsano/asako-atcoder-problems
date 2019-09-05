from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(str(type(var)) + name +":" + " = " + repr(var), file=stderr)
    return


def main():
    A, B, C = list(map(int,input().split()))
    print(A,B,C)
    # N = int(input())
    # a = [int(input()) for _ in range(N)]
    # S = str(input())[:-1]
    # print(S)
    # L = len(S)
    # INF = 10000000002
    # EPS = 1e-9
    # exit()



if __name__ == "__main__":
    main()
