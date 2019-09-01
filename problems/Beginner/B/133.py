from sys import exit, stderr, stdin
input = stdin.readline
def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    N,D = [int(n) for n in input().split()]
    ans = 0
    X = [[0 for __ in range(D)] for _ in range(N)]
    for i in range(N):
        X[i] = [int(n) for n in input().split()]
    # print(X)
    for i in range(N):
        d = 0
        for j in range(i+1,N):
            d = sum([pow(y-z,2) for y,z in zip(X[i],X[j])])
            # print(d)
            d **= 0.5
            if d/1 == d//1:
                ans += 1
    print(ans)
if __name__ == "__main__":
    main()
