
P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))


def gcd(a, b):  # greatest common divisor
    if (a < b):
        a, b = b, a
    while(b > 0):
        a, b = b, a % b
    return a


a = abs(P1[0]-P2[0])
b = abs(P1[1]-P2[1])
g = gcd(a, b)
print(g-1)
