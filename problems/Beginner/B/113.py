from sys import exit
N = int(input())
T,A = [int(n) for n in input().split()]
H = [int(n) for n in input().split()]
mnear = 0
mint = (1 << 20)
for i in range(N):
    # print(T - H[i]*0.006)
    if abs(A - (T - H[i]*0.006)) < mint:
        mint = abs(A - (T - H[i]*0.006))
        mnear = i

print(mnear+1)
exit()
