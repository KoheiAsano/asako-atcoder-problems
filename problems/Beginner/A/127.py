# from sys import exit
A, B = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
if A >= 13:
    print(B)
elif 6 <= A <= 12:
    print(B//2)
else:
    print(0)
