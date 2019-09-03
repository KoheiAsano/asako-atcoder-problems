from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    N, D = map(int,input().split())
    if (D==1):
        print(0)
        exit()
    D-=N
    ans = 1
    while(D>0):
        ans +=1
        D -= N-1
    print(ans)

if __name__ == "__main__":
    main()
