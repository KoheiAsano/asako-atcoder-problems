import sys
# N,M = [int(n) for n in input().split()]
# S = str(input())
# T = str(input())
a,b,c = [int(n) for n in input().split()]

if(b <= c and a <= c):
    print(10*c + a + b)
elif(a <= b and c <= b):
    print(10*b + c + a)
elif(c <= a and b <= a):
    print(10*a + c + b)
