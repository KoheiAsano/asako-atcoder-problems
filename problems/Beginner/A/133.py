from sys import exit, stderr, stdin
input = stdin.readline
def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    N, A, B = [int(n) for n in input().split()]
    print(min(A*N, B))



if __name__ == "__main__":
    main()
