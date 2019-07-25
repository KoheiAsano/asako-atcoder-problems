from sys import exit, stderr
def debug(var, name="hoge"):
    print(name + str(id(var)) +" = " + repr(var), file=stderr)
    return
# A, B, C = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# INF = 10000000002
# EPS = 1e-9
# exit()
