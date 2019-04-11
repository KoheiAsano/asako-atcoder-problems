from sys import exit
# A,B,C = [int(n) for n in input().split()]
# N = int(input())
a = [int(input()) for _ in range(5)]
k = int(input())
for e0 in a:
    for e1 in a:
        if abs(e0 - e1) > k:
            print(":(")
            exit()
print("Yay!")
# S = str(input())
# L = len(S)
# T = str(input())
# exit()
