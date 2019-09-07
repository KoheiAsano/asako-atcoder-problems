from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    K, A = [int(n) for n in input().split()]
    for i in range(-K+1,K):
        print(A+i,end=" ")
    print()



if __name__ == "__main__":
    main()
