# from sys import exit
r, D, x2000 = [int(n) for n in input().split()]

tmp = x2000
for i in range(10):
    tmp = r * tmp - D
    print(tmp)
