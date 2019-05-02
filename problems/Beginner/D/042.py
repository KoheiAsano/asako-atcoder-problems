from sys import exit
H,W,A,B = [int(n) for n in input().split()]
MOD = 10**9+7
NUM = 2*10**5

fact=[1]*(NUM+1)
factinv=[1]*(NUM+1)
for i in range(1,NUM+1):
    fact[i]=(fact[i-1]*i)%MOD

factinv[NUM]=pow(fact[NUM],MOD-2,MOD)
for i in range(NUM,0,-1):
    factinv[i-1]=(factinv[i]*i) % MOD
ans=0
for i in range(B,W):
    tmp0 = fact[i+H-A-1]
    tmp0 *= factinv[H-A-1]
    tmp0 %= MOD
    tmp0 *= factinv[i]
    tmp0 %= MOD

    tmp1 = fact[W-i-1+A-1]
    tmp1 *= factinv[W-i-1]
    tmp1 %= MOD
    tmp1 *= factinv[A-1]
    tmp1 %= MOD
    ans += (tmp0 * tmp1) % MOD
    ans %= MOD
print(ans)
