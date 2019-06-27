# mod nの体におけるaの逆元
def modinv(a, m):
    b = m
    u = 1
    v = 0
    while(b):
        t = a//b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if(u < 0):
        u += m
    return u


def inverse(a, m):
    t, next_t = 0, 1
    r, next_r = m, a
    while next_r != 0:
        q = r // next_r
        t, next_t = next_t, t - q * next_t
        r, next_r = next_r, r - q * next_r
    if t < 0:
        t += m
    return t

MOD = 1000000007
a = 12345678900000
b = 100000
print(a//b)
a %= MOD
print(a * modinv(b, MOD) % MOD)
print(a * inverse(b, MOD) % MOD)
