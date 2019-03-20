from sys import exit

S,T = [str(n) for n in input().split()]
if S == T:
    print("=")
    exit()
print(">" if S>T else "<")
# L = len(S)
# T = str(input())
exit()
