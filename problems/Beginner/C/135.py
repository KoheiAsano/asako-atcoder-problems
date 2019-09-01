from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return


def main():
    N = int(input())
    A = [int(n) for n in input().split()]
    B = [int(n) for n in input().split()]
    ans = 0
    for i in range(N, -1, -1):
        # print(A)
        # print(B)
        if A[i] > 0:
            if i != N:
                beat = min(B[i],A[i])
                ans += beat
                A[i]-=beat
                B[i]-=beat
                if A[i] == 0:
                    continue
            beat = min(B[max(0,i-1)],A[i])
            ans += beat
            A[i]-=beat
            B[max(0,i-1)]-=beat
    # print(A)
    # print(B)
    print(ans)







if __name__ == "__main__":
    main()
