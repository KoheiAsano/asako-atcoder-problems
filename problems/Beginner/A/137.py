from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    A, B = [int(n) for n in input().split()]
    print(max(A-B, A+B, A*B))



if __name__ == "__main__":
    main()
