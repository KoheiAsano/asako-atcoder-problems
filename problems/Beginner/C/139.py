from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    N = int(input())
    H = list(map(int,input().split()))
    cnt = 0
    ans = 0
    H[0]
    for i in range(1,N):
        if H[i-1] >= H[i]:
            cnt += 1
            ans = max(cnt,ans)
        else:
            cnt =0
    print(ans)
if __name__ == "__main__":
    main()
