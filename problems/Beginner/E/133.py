from sys import exit, stderr, stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**7)
def debug(var, name="hoge"):
    print(name +":" + str(type(var)) + " = " + repr(var), file=stderr)
    return




MOD = 10**9+7
NUM = 10**5 + 2

fact = [1] * (NUM + 1)
fact_inv = [1] * (NUM + 1)

for i in range(1, NUM+1):
    fact[i] = (fact[i-1]*i) % MOD
# フェルマーの少定理から(a**MOD-1)が1 => (a**MOD-2)がaの逆元
fact_inv[NUM] = pow(fact[NUM], MOD-2, MOD)

# 階乗の逆元は、逆元の階乗なので、(n-1)!の逆元を求めたいなら(n!の逆元)*nでOK
for i in range(NUM, 2, -1):
    fact_inv[i-1] = (fact_inv[i]*i) % MOD

def perm(n,k):
    if n<k or k<0:
        return 0
    else:
        return (fact[n]*fact_inv[n-k])% MOD



def main():
    N, K = map(int,input().split())

    adjl = [[] for _ in range(N)]
    for _ in range(N-1):
        a ,b = map(int,input().split())
        a ,b = a-1, b-1
        adjl[a].append(b)
        adjl[b].append(a)
    deg = [len(n) for n in adjl]

    def count(n, parent = None):
        # ルートなら親を含めたその子の塗り方
        if parent is None:
            c = perm(K,deg[n]+1)
        # それ以外なら自分と親が決まってるので子の塗り方
        else:
            c = perm(K-2,deg[n]-1)
        for neigh in adjl[n]:
            if neigh == parent:
                continue
            c *= count(neigh,n)
            c %= MOD
        return c
    print(count(0))





if __name__ == "__main__":
    main()
