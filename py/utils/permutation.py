MOD = 10**9+7
NUM = 20

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
