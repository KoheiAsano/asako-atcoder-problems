from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    N = int(input())
    p = [int(n) for n in input().split()]
    sp = sorted(p)
    cnt = 0
    for i in range(N):
        if p[i] != sp[i]:
            cnt += 1

    print("YES" if cnt <= 2 else "NO")





if __name__ == "__main__":
    main()
