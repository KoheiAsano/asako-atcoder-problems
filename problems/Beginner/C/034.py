from sys import exit
W,H = [int(n)-1 for n in input().split()]
MOD = 10**9+7
# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
def modfact(n, m):
    res=1
    for i in range(2,n+1):
        res*=i
        res%=m
    return res

def modinv0(a, m):
    b=m
    u=1
    v=0
    while(b):
        t = a//b
        a -= t * b
        a,b = b,a
        u -= t*v
        u,v = v,u
    u %=m
    if(u < 0):
        u+= m
    return u

denominator = modfact(H,MOD) * modfact(W,MOD)
numerator = modfact(H+W,MOD)
print((numerator * modinv0(denominator, MOD)) % MOD)
