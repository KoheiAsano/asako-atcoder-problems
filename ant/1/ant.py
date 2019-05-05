from sys import exit
L = int(input())
n = int(input())
x = sorted([int(n) for n in input().split()])
middle = L/2
d = 10**8

for e in x:
    tmp = abs(middle -e)
    if d > tmp:
        d = tmp
        minans = e
    else:
        break
print(min(L - minans, minans))
print(max(L - x[0], L- x[-1]))
