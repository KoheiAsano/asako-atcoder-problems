from sys import exit, stderr, stdin
input = stdin.readline
def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    L, R = [int(n) for n in input().split()]
    if (L//2019)<(R//2019):
        print(0)
    else:
        l = L%2019
        r = R%2019
        res = 2019**2
        for i in range(l,r+1):
            for j in range(i+1,r+1):
                res = min(res,(i*j)%2019)
        print(res)


if __name__ == "__main__":
    main()
