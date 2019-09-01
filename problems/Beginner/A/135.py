from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    A, B = [int(n) for n in input().split()]

    print((A+B)//2 if (A+B)%2 == 0 else "IMPOSSIBLE")



if __name__ == "__main__":
    main()
