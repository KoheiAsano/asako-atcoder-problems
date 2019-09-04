from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return

def gau(n):
    return n*(n+1)//2

def main():
    N = int(input())
    if (N==1):
        print(0)
    else:
        print(gau(N-1))

if __name__ == "__main__":
    main()
