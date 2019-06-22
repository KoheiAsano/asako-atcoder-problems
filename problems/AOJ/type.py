
N = int(input())
for i in range(N):
    S = str(input())
    bit = bin(int(S, 16))[2:].zfill(32)

    bit = bit[::-1]
    # print(bit)
    pos = (-1)**int(bit[31])
    up = int(bit[7:31][::-1], 2)
# print(bit[7:31],len(bit[7:31]), int(bit[7:31], 2))
    # print(bit[:7],len(bit[:7]))

    # print(up)
    low = 0
    pow = 0.5
    for b in bit[:7][::-1]:
        # print(pow*int(b))
        low = low + pow*int(b)
        # print(int(b))
        pow *= 0.5
    # print(low)

    print(pos*(up+low))
