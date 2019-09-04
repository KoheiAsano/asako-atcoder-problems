from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return

def main():
    S = str(input())[:-1]
    T = str(input())[:-1]
    SL = len(S)
    TL = len(T)
    graph = [[] for _ in range(SL)]

    MOD = 10 ** 16 + 61
    base = 12345
    base_inv = pow(base,MOD-2,MOD)
    power = [1] * (LS+LT)
    power_inv = [1] * (LS+LT)
    for n in range(1,LS+LT):
        power[n] = power[n-1] * base % MOD
        power_inv[n] = power_inv[n-1] * base_inv % MOD
    def rollhash(s):
        res = [0]*(len(s)+1)
        for i in range(len(s)):
            res[i+1] = (res[i] + power[i] * ord(s[i])) % MOD
        return res
if __name__ == "__main__":
    main()
