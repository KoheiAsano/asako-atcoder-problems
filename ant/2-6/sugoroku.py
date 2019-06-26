def exteuclid(f, g, a, b):
    if(g == 0):
        return (f, 1, 0)
    else:
        d, a, b = exteuclid(g, f % g, a, b)
        before_a = b
        before_b = a - b*(f//g)
        return (d, before_a, before_b)


def euclid_ext(a, b):
    if(b == 0):
        # print(a, 1, b, 0, a, 1)
        return (a, 1, 0)
    else:
        d, y, x = euclid_ext(b, a % b)
        y -= (a//b)*x
        # print(a, x, b, y, d, a//b)
        return (d, x, y)


a, b = list(map(int, input().split()))

# print(euclid_ext(a, b))

d, x, y = exteuclid(a, b, 0, 0)
if d != 1:
    print(-1)
else:
    px = 0 if x < 0 else x
    py = 0 if y < 0 else y
    nx = -x if x < 0 else 0
    ny = -y if y < 0 else 0
    print(px, py, nx, ny)
