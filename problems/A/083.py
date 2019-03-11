from sys import exit
A,B,C,D = [int(n) for n in input().split()]
L = A+B
R = C+D
if L > R:
    print("Left")
elif L == R:
    print("Balanced")
else:
    print("Right")
