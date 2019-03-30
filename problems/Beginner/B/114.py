from sys import exit
# A,B,C = [int(n) for n in input().split()]
# a = [int(input()) for _ in range(N)]
S = str(input())
L = len(S)
# T = str(input())
# exit()
mind = 119000000000
for i in range(L-2):
    if abs(753 - int(S[i]+S[i+1]+S[i+2])) < mind:
        mind = abs(753 - int(S[i]+S[i+1]+S[i+2]))
print(mind)
