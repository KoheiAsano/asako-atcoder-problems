from sys import exit, stderr, stdin
input = stdin.readline
def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    N = int(input())
    A = [int(n) for n in input().split()]

    X1 = sum(A) - 2*sum([a for a in A[1::2]])
    ans = [str(X1)]
    for i in range(1,N):
        ans.append(str(2*A[i-1]-int(ans[-1])))
    print(" ".join(ans))



if __name__ == "__main__":
    main()
