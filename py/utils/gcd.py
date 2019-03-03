def gcd(a,b):#greatest common divisor
    if (a<b):
        tmp = a
        a = b
        b = tmp
    r = 10
    while(r>0):
        r = a%b
        a = b
        b = r
    return a
print(gcd(17,42))
print(gcd(42,17))

print(gcd(17,34))
print(gcd(34,17))

def lcm(a,b):#least common multiple
    return int(a*b/gcd(a,b))
print(lcm(17,42))
print(lcm(42,17))

print(lcm(17,34))
print(lcm(34,17))
