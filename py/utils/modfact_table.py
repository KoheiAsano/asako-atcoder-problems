MOD = 10**9+7
NUM = 2*10**5

fact=[1]*(NUM+1)
factinv=[1]*(NUM+1)
for i in range(1,NUM+1):
    fact[i]=(fact[i-1]*i)%MOD

factinv[NUM]=pow(fact[NUM],MOD-2,MOD)
for i in range(NUM,0,-1):
    factinv[i-1]=(factinv[i]*i) % MOD
