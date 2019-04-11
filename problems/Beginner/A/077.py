from sys import exit
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
# a = [int(input()) for _ in range(N)]
S = str(input())
S1 = str(input())[::-1]
if (S == S1):
    print("YES")
else: 
    print("NO")
